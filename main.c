#include <avr/io.h>
#include <avr/interrupt.h>

int main(void){
    CCP = 0xD8;
    CLKPSR = 0;
    DDRB |= (1 << 2);

    OSCCAL = 0x82;
    //TCCR0A |= (1 << WGM00);
    TCCR0B |= (1 << WGM02) | (1 << CS00);
    TIMSK0 |= (1 << OCIE0A) | (1 << TOIE0);

    OCR0A = 100;

    sei();
    for(;;){
        //PORTB ^= (1 << 2);
    }
}

ISR(TIM0_COMPA_vect){
    PORTB ^= (1 << 2);
}

