MCU = attiny2313
TARGET = main
AVRDUDE_PROGRAMMER = atmelice_isp
FCPU=18432000UL

BUILDDIR=build

OPT = s
SRC = $(shell find src -name '*.c')
#SRC = main.c

FORMAT = ihex

# List any extra directories to look for include files here.
#     Each directory must be seperated by a space.
EXTRAINCDIRS = inc

#### Flags ####
CFLAGS = -mmcu=$(MCU) -I. \
-g -O$(OPT) \
-funsigned-char -funsigned-bitfields -fpack-struct -fshort-enums \
-Wall -Wstrict-prototypes \
-Wa,-adhlns=$(<:src/%.c=$(BUILDDIR)/%.lst) \
-DF_CPU=$(FCPU)\
$(patsubst %,-I%,$(EXTRAINCDIRS))\
-std=gnu99 
#-fno-builtin 

LDFLAGS = -Wl,-Map=$(BUILDDIR)/$(TARGET).map,--cref
# Minimalistic printf version
#LDFLAGS += -Wl,-u,vfprintf -lprintf_min

# Floating point printf version (requires -lm below)
#LDFLAGS += -Wl,-u,vfprintf -lprintf_flt

# -lm = math library
LDFLAGS += -lm
#LDFLAGS += -nostdlib

AVRDUDE_FLAGS = -p $(MCU) -c $(AVRDUDE_PROGRAMMER) -U flash:w:$(BUILDDIR)/$(TARGET).hex

#### Define programs and commands. ####
CC = avr-gcc

OBJCOPY = avr-objcopy
OBJDUMP = avr-objdump
SIZE = avr-size
AVRDUDE = avrdude


REMOVE = rm -f
COPY = cp

# Define all object files.
OBJ = $(SRC:src/%.c=$(BUILDDIR)/%.o) 

# Define all listing files.
LST = $(SRC:src/%.c=$(BUILDDIR)/%.lst)

# Default target: make program!
all: $(TARGET).elf
#	$(BUILDDIR)/$(TARGET).lss $(BUILDDIR)/$(TARGET).sym 
#	$(AVRDUDE) $(AVRDUDE_FLAGS) $(AVRDUDE_WRITE_FLASH) $(AVRDUDE_WRITE_EEPROM)

# Program the device.  
program: $(BUILDDIR)/$(TARGET).hex $(BUILDDIR)/$(TARGET).eep
	$(AVRDUDE) $(AVRDUDE_FLAGS)


# Create final output files (.hex, .eep) from ELF output file.
$(BUILDDIR)/%.hex: %.elf
	@echo
	@echo "creating ihex"
	$(OBJCOPY) -O $(FORMAT) -R .eeprom $< $@

$(BUILDDIR)/%.eep: %.elf
	@echo
	@echo "eeprom"
	-$(OBJCOPY) -j .eeprom --set-section-flags=.eeprom="alloc,load" \
	--change-section-lma .eeprom=0 -O $(FORMAT) $< $@

# Create extended listing file from ELF output file.
$(BUILDDIR)/%.lss: %.elf
	@echo
	@echo "listing"
	$(OBJDUMP) -h -S $< > $@

# Create a symbol table from ELF output file.
$(BUILDDIR)/%.sym: %.elf
	@echo
	@echo "symbol table"
	avr-nm -n $< > $@



# Link: create ELF output file from object files.
#.SECONDARY : $(BUILDDIR)/$(TARGET).elf
#.PRECIOUS : $(OBJ)
$(TARGET).elf: $(OBJ)
	@echo 
	@echo "linking: " $(OBJ)
	$(CC) $(CFLAGS) $(OBJ) --output $@ $(LDFLAGS)


# Compile: create object files from C source files.
$(BUILDDIR)/%.o : src/%.c
	@echo
	@echo "compiling" $<
	$(CC) -c $(CFLAGS) $< -o $@


# Target: clean project.
clean: 
	@echo
	@echo "cleaning"
	$(REMOVE) $(BUILDDIR)/$(TARGET).hex
	$(REMOVE) $(BUILDDIR)/$(TARGET).eep
	$(REMOVE) $(BUILDDIR)/$(TARGET).obj
	$(REMOVE) $(BUILDDIR)/$(TARGET).cof
	$(REMOVE) $(TARGET).elf
	$(REMOVE) $(BUILDDIR)/$(TARGET).map
	$(REMOVE) $(BUILDDIR)/$(TARGET).obj
	$(REMOVE) $(BUILDDIR)/$(TARGET).a90
	$(REMOVE) $(BUILDDIR)/$(TARGET).sym
	$(REMOVE) $(BUILDDIR)/$(TARGET).lnk
	$(REMOVE) $(BUILDDIR)/$(TARGET).lss
	$(REMOVE) $(OBJ)
	$(REMOVE) $(LST)
	$(REMOVE) $(SRC:src/%.c=$(BUILDDIR)/%.s)
	$(REMOVE) $(SRC:src/%.c=$(BUILDDIR)/%.d)
	$(REMOVE) $(BUILDDIR)/*~

# Automatically generate C source code dependencies. 
# (Code originally taken from the GNU make user manual and modified 
# (See README.txt Credits).)
#
# Note that this will work with sh (bash) and sed that is shipped with WinAVR
# (see the SHELL variable defined above).
# This may not work with other shells or other seds.
#
$(BUILDDIR)/%.d: %.c
	set -e; $(CC) -MM $(CFLAGS) $< \
	| sed 's,\(.*\)\.o[ :]*,\1.o \1.d : ,g' > $@; \
	[ -s $@ ] || rm -f $@


# Remove the '-' if you want to see the dependency files generated.
-include $(SRC:.c=.d)

# Listing of phony targets.
.PHONY : all clean program

