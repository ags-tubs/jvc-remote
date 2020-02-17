#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "uart.h"

volatile uint8_t connected=0;
volatile uint8_t rx_flag=0;

void setup(){
    /* clock config */
    CCP = 0xD8;
    CLKPSR = 0;
    OSCCAL = 0x81;

    uart_init();
    sei();
}

void rx_action(uint8_t c, uint8_t error){
    if(c == 0x80)
        connected = 0;
    rx_flag = 1;
}

uint8_t wait_rx(){
    rx_flag=0;
    while(!rx_flag);
    _delay_us(500);
    return 0x80;
}

inline void send_cmd(uint8_t cmd, uint8_t data){
    uart_putchar(0x83);

    wait_rx();

    uart_putchar(data | 0x40);
    uart_putchar(cmd);
    uart_putchar(((data | 0x40) + cmd) & 0x7F);
    
    wait_rx();
}
   
inline void special_xfer(uint8_t data){
    uart_putchar(0x90 | data);
    wait_rx();
}

int main(void){
    setup();
    set_rx_handler(&rx_action);

    uint8_t tally_in;
    uint8_t tally_in_old=2;

    for(;;){
        while(!connected){
            uart_putchar(0x80);
            if(wait_rx() == 0x80){
                uart_putchar(0xA0);
                connected = 1;
            }
            send_cmd(0,0);
            send_cmd(0x7d,0x01);
            special_xfer(0);
        }
        if(connected){
            tally_in = PINB & (1 << 0);
            if(tally_in != tally_in_old)
                send_cmd(0x08, tally_in_old);
            tally_in_old = tally_in;
        }
    }
}

