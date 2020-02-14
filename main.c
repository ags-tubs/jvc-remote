#include <avr/io.h>
#include <avr/interrupt.h>

#define TX_PIN 2

uint8_t tx_bit_state = 0;
uint8_t tx_byte = 'a';

void tx(){
    if(tx_bit_state == 0)
        PORTB &= ~(1 << TX_PIN);
    else if(tx_bit_state < 9)
        PORTB = ((tx_byte >> tx_bit_state-1) & 0x01)<<TX_PIN;
    else
        PORTB |= (1 << TX_PIN);
}

int main(void){
    CCP = 0xD8;
    CLKPSR = 0;
    DDRB |= (1 << 2);

    OSCCAL = 0x82;
    //TCCR0A |= (1 << WGM00);
    TCCR0B |= (1 << WGM02) | (1 << CS01);
    TIMSK0 |= (1 << OCIE0A) | (1 << TOIE0);

    OCR0A = 104;

    sei();
    for(;;){
        //PORTB ^= (1 << 2);
    }
}

ISR(TIM0_COMPA_vect){
    tx_bit_state++;
    tx();
}

