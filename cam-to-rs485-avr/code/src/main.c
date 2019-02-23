#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>

#define BAUD 9600
#define MYUBRR F_CPU/16/BAUD-1

volatile int state = 0;

volatile int connection=0;
volatile int cmd_val=0;

void USART_Init(unsigned int ubrr)
{
  /*Set baud rate */
  UBRRH = (unsigned char)(ubrr>>8);
  UBRRL = (unsigned char)ubrr;
  /*Enable receiver and transmitter */
  //UCSRB = (1<<RXEN) | (1<<TXEN) | (1<<RXCIE);
  UCSRB = (1<<RXEN) | (1<<RXCIE);
  /* Set frame format: 8data, 1 stop bit */
  UCSRC = (1<<UCSZ0) | (1 << UCSZ1) | (1 << UPM1);
}
void USART_Transmit(unsigned char data )
{
  /* Wait for empty transmit buffer */
  while ( !( UCSRA & (1<<UDRE)) )
    ;
  /* Put data into buffer, sends the data */
  UDR = data;
}


int main(void){
    DDRB |= (1<<0);

    DDRD |= (1<<3);
    DDRD |= (1<<4);
    DDRD |= (1<<5);

    DDRB |= (1<<0);

    GIMSK = 1<<INT0;	
    MCUCR = 1<<ISC01 | 0<<ISC00;

    TCCR0B &= ~((1<<CS00) | (1<<CS00)); 
    TIMSK |= 1 << OCIE0B;

    USART_Init(MYUBRR);

    sei();

    PORTD |= (1<<5);
    PORTD |= (1<<4);
    while (1){
        _delay_ms(1000);
    }
}

ISR(INT0_vect)
{
    if(!state){
        state=1;


        UCSRB &= ~((1<<RXEN) | (1<<RXCIE));
        DDRD |= (1<<0);
        PORTD |= (1 << 0);

        PORTD |= 1 << 3;

        TCNT0 = 0;
        TCCR0B |= (0<<CS00) | (0<<CS01) | (1<<CS02); 
        OCR0B=0x4B;
    }
}

ISR(TIMER0_COMPB_vect){
    PORTD &= ~(1 << 3);

    DDRD &= ~(1<<0);
    PORTD &= ~(1 << 0);
    UCSRB |= (1<<RXEN) | (1<<RXCIE);

    TCCR0B &= ~((1<<CS00) | (1<<CS01) | (1<<CS02)); 
    state=0;
}

ISR (USART_RX_vect)
{
    uint8_t data = UDR;
    if(connection==0 && data == 0x83){
        PORTD&=~(1<<5);
        connection=1;
        return;
    }
    if(connection == 1){
        cmd_val=data;
        connection = 2;
        return;
    }
    if(connection == 2){
        if(data==0x08){
            PORTB = (PORTB & ~(1<<0))|((cmd_val & 0x1)<<0);
            PORTD = (PORTD & ~(1<<4))|(~(cmd_val & 0x1)<<4);
        }
        connection = 3;
        return;
    }
    if(connection == 3){
        connection=0;
        PORTD|=1<<5;
        return;
    }
}
