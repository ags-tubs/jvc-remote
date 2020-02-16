#include <avr/io.h>
#include <avr/interrupt.h>
#include "uart.h" 

volatile uint8_t tx_bit_state = 10;
volatile uint8_t tx_byte = 0;
volatile uint8_t tx_busy = 0;

void uart_init(){
    DDRB |= (1 << TX_PIN) | (1<<1);
    PORTB |= (1 << TX_PIN);

    // no prescaler, count up to OCR0A
    TCCR0B |= (1 << WGM02) | (1 << CS00);
    TIMSK0 |= (1 << OCIE0A);

    // 8MHz / 833 = 9603 baud
    OCR0A = 833;
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
            PORTB = ((tx_byte >> (tx_bit_state-1)) & 0x01)<<TX_PIN;
            break;
#if UART_PARITY_MODE == PARITY_EVEN
        case UART_PARITY_BIT:
            for(uint8_t i=0;i<8;i++)
                if(tx_byte & (1<<i))
                    high_bits++;

            if(high_bits&0x01)
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

int uart_putchar(char c){
    while(tx_busy);
    tx_busy = 1;
    tx_byte = c;
    tx_bit_state = 0;
    return 0;
}

ISR(TIM0_COMPA_vect){
    tx();
}
