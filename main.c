#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "uart.h"

void setup(){
    /* clock config */
    CCP = 0xD8;
    CLKPSR = 0;
    OSCCAL = 0x82;

    uart_init();
    sei();
}

int main(void){
    setup();
    for(;;){
        uart_putchar('t');
        uart_putchar('e');
        uart_putchar('s');
        uart_putchar('t');
        uart_putchar('\n');
        uart_putchar('\r');
        _delay_ms(1000);
    }
}

