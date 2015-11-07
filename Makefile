ifeq ($(OS),Windows_NT)
	RM=del
else
	RM=rm -f
endif

# Directories
INCLUDE=include
BUILD=build
SRC=src

# Compiler flags
CFLAGS= -g -Wall -Wextra -O3

# Choose your favorite compiler
#CC = gcc $(CFLAGS)
CC = clang $(CFLAGS)

OBJECTS=$(BUILD)/congruencial_generators $(BUILD)/imsl
SRCS=$(SRC)/*.c

all: $(OBJECTS)

$(OBJECTS): $(SRCS)
	$(CC) -I $(INCLUDE)/*.h $(SRCS) -o $@

.PHONY: clean

clean:
	rm -f $(BUILD)/*.o

