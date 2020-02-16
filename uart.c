#include <avr/io.h>
#include <avr/interrupt.h>
#include "uart.h" 

volatile uint8_t tx_bit_state = 10;
volatile uint8_t tx_byte = 0;
volatile uint8_t tx_busy = 0;

volatile uint8_t rx_byte = 0;
volatile uint8_t rx_bit_state = 0;
volatile uint8_t rx_error = 0;

void uart_init(){
    DDRB |= (1 << TX_PIN) | (1<<0);
    PORTB |= (1 << TX_PIN);

    // no prescaler, count up to OCR0A
    TCCR0B |= (1 << WGM02) | (1 << CS00);
    TIMSK0 |= (1 << OCIE0A); // TX interrupt

    // RX interrupt; will be enabeled while rx'ing data
    //TIMSK0 |= (1 << OCIE0B);

    OCR0A = UART_TIMER_VAL;

    PCICR |= (1 << PCIE0);
    PCMSK |= (1 << RX_PIN);
}

int uart_putchar(char c){
    while(tx_busy);
    tx_busy = 1;
    tx_byte = c;
    tx_bit_state = 0;
    return 0;
}

void tx(){
#if UART_PARITY_MODE != PARITY_NONE
    uint8_t high_bits = 0;
#endif
    switch(tx_bit_state){
        case UART_START_BIT:
            PORTB &= ~(1 << TX_PIN);
            break;
        case UART_DATA_FIRST_BIT ... UART_DATA_LAST_BIT:
            PORTB = (PORTB & ~(1<<TX_PIN)) | ((tx_byte >> (tx_bit_state-1)) & 0x01)<<TX_PIN;
            break;
#if UART_PARITY_MODE != PARITY_NONE
        case UART_PARITY_BIT:
            /* calculate parity */
            for(uint8_t i=0;i<8;i++)
                if(tx_byte & (1<<i))
                    high_bits++;

#if UART_PARITY_MODE == PARITY_EVEN
            if(high_bits&0x01)
#elif UART_PARITY_MODE == PARITY_ODD
            if(!high_bits&0x01)
#endif
                PORTB |= (1 << TX_PIN);
            else
                PORTB &= ~(1 << TX_PIN);
            break;
#endif
        case UART_STOP_BIT:
            PORTB |= (1 << TX_PIN);
            break;
        case UART_STOP_BIT+1:
            tx_busy = 0;
            return;
            break;
    }
    tx_bit_state++;
}

void rx(){
    switch(rx_bit_state){
        case UART_START_BIT:
            rx_byte=0;
            if(PINB & (1 << RX_PIN))
                rx_error = 1;
            break;
        case UART_DATA_FIRST_BIT ... UART_DATA_LAST_BIT:
            if(PINB & (1 << RX_PIN))
                rx_byte |= (1 << (rx_bit_state-1));
            break;
        case UART_STOP_BIT:
            rx_bit_state=0;

            /* diable RX routine */
            TIMSK0 &= ~(1 << OCIE0B);

            /* clear old flag an wait for new falling edge */
            PCMSK |= (1 << RX_PIN);

            return;
            break;
    }
    rx_bit_state++;
}

ISR(TIM0_COMPA_vect){
    tx();
}

ISR(TIM0_COMPB_vect){
    rx();
}

ISR(PCINT0_vect){
    if(!(PINB & (1<<RX_PIN))){ /* falling edge only */
        /* disable PCINT while transmissions is in progress */
        PCMSK &= ~(1 << RX_PIN);

        /* sample at middle of bit */
        OCR0B = (TCNT0 + 200) % 833; //TODO fix parametric
        //OCR0B = (TCNT0 + (UART_TIMER_VAL/2)) % UART_TIMER_VAL;

        /* enable RX routine */
        TIMSK0 |= (1 << OCIE0B);
    }
}
