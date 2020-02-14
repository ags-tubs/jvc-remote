TARGET  = main
FILES   = main
MCU     = attiny10
PROGC	= t10
CC      = avr-gcc
TOOL    = avrispmkII

BUILDDIR = build

DEFINES = -DF_CPU=8000000UL
 
CFLAGS  =-mmcu=$(MCU) -O2 -Wall $(DEFINES) -std=c99 -ffunction-sections -fdata-sections
LDFLAGS =-mmcu=$(MCU) -Wl,--gc-sections

LDFILES = $(foreach FILE,$(FILES),$(BUILDDIR)/$(FILE).o)

all: clean $(BUILDDIR)/$(TARGET).elf

$(BUILDDIR)/%.o: %.c
	mkdir -p $(BUILDDIR)
	$(CC) $(CFLAGS) -c $< -o $(BUILDDIR)/$*.o

$(BUILDDIR)/$(TARGET).elf: $(LDFILES)
	mkdir -p $(BUILDDIR)
	$(CC) $(LDFLAGS) $(LDFILES) -o $(BUILDDIR)/$(TARGET).elf

$(BUILDDIR)/$(TARGET).hex : $(BUILDDIR)/$(TARGET).elf
	 avr-objcopy -j .data -j .text -O ihex $< $@

fuse: 
	avrdude -p $(PROGC) -c $(TOOL) -U lfuse:w:0xE8:m -U hfuse:w:0xD1:m

load: $(BUILDDIR)/$(TARGET).hex
	avrdude -p $(PROGC) -c $(TOOL) -U flash:w:$(BUILDDIR)/$(TARGET).hex -v -B 2

program: clean load
	
size: $(BUILDDIR)/$(TARGET).elf
	avr-size -C --mcu=$(MCU) $(BUILDDIR)/$(TARGET).elf

.PHONY=clean
clean:
	rm -rf $(BUILDDIR)
