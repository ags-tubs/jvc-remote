#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#define TX_PIN 2

volatile uint8_t tx_bit_state = 10;
volatile uint8_t tx_byte = 'a';
volatile uint8_t tx_busy = 0;

void tx(){
    if(tx_bit_state == 0){
        PORTB &= ~(1 << TX_PIN);
    }
    else if(tx_bit_state < 9)
        PORTB = ((tx_byte >> (tx_bit_state-1)) & 0x01)<<TX_PIN;
    else if(tx_bit_state == 9){
        PORTB |= (1 << TX_PIN);
        tx_bit_state=9;
    }
    else if(tx_bit_state == 10){
        tx_busy = 0;
        return;
    }
    tx_bit_state++;
}

int uart_putchar(char c){
    PORTB |= (1<<1);
    while(tx_busy);
    PORTB &= ~(1<<1);
    tx_busy = 1;
    tx_byte = c;
    tx_bit_state = 0;
    return 0;
}

int main(void){
    CCP = 0xD8;
    CLKPSR = 0;

    DDRB |= (1 << TX_PIN) | (1<<1);
    PORTB |= (1 << TX_PIN);

    OSCCAL = 0x82;
    //TCCR0A |= (1 << WGM00);
    TCCR0B |= (1 << WGM02) | (1 << CS00);
    TIMSK0 |= (1 << OCIE0A) | (1 << TOIE0);

    // 8MHz / 833 = 9603
    OCR0A = 833;

    sei();
    for(;;){
        uart_putchar('a');
        uart_putchar('b');
        uart_putchar('c');
        _delay_ms(1000);
    }
}

ISR(TIM0_COMPA_vect){
    tx();
}

