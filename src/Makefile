ifeq ($(OS),Windows_NT)
	RM=del
else
	RM=rm -f
endif

INCLUDE=/opt/TestU01/include
LIB=/opt/TestU01/lib

# Compiler flags
CFLAGS= -g -Wall -Wextra -O3

# Choose your favorite compiler
#CC = gcc $(CFLAGS)
CC = clang $(CFLAGS)

OBJECT=SmallCrush
SRC=SmallCrush.c

all: $(OBJECT)

$(OBJECT): $(SRC)
	$(CC) -I $(INCLUDE) $(SRC) -o $@ -L$(LIB) -ltestu01 -lprobdist -lmylib -lm

.PHONY: clean

clean:
	rm -f *.o
