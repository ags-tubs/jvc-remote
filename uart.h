#ifndef _UART_H_
#define _UART_H_

/* User Config */
#define TX_PIN 2
#define RX_PIN 1

#define UART_BAUD 9600
#define UART_PARITY_MODE PARITY_EVEN
#define UART_DATA_LAST_BIT 8
/* User Config End */

#define UART_TIMER_VAL F_CPU/UART_BAUD
// 8MHz / 833 = 9603 baud

#define PARITY_NONE 0
#define PARITY_EVEN 1
#define PARITY_ODD 2

#define UART_START_BIT 0
#define UART_DATA_FIRST_BIT 1

#if UART_PARITY_MODE == PARITY_NONE
#define UART_STOP_BIT UART_DATA_LAST_BIT+1
#else
#define UART_PARITY_BIT UART_DATA_LAST_BIT+1
#define UART_STOP_BIT UART_DATA_LAST_BIT+2
#endif

void uart_init();
void uart_putchar(char c);
void set_rx_handler(void (* handler)(uint8_t, uint8_t));

extern volatile uint8_t rx_byte;

#endif
