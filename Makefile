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
INCLUDES=$(INCLUDE) /opt/TestU01/include
LIB=/opt/TestU01/lib
SRCS=$(SRC)/congruencial_generators.c $(SRC)/imsl.c

all: $(OBJECTS)

$(OBJECTS): $(SRCS)
	$(CC) -I /include/ -I/opt/TestU01/include/ $(SRCS) -o $@ -L$(LIB) -ltestu01 -lprobdist -lmylib -lm

.PHONY: clean

clean:
	rm -f $(BUILD)/*.o

