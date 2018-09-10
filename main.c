#include <limits.h>
#include <stdio.h>
#include "holberton.h"

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
	int len;
	int len2;
	unsigned int ui;
	void *p = (void *)-1;
/*	void *addr;
	_printf("%a");
	printf("\n");
        printf("%a");
*/	printf("\n");
	_printf("%c\n", 'a');
	printf("%c\n", 'a');
	len = _printf("Let's try to printf a simple sentence.\n");
	len2 = printf("Let's try to printf a simple sentence.\n");
	ui = (unsigned int)INT_MAX + 1024;
/*	addr = (void *)0xe7ffe637541f0;*/
	len = _printf("%p", NULL);
	len2 = printf("%p", NULL);
	printf("len is %i, len2 is %i\n", len, len2);
	len = _printf("Can you print an address?\n%p\nNice!\n", p);
	len2 = printf("Can you print an address?\n%p\nNice!\n", p);
	printf("len is %i, len2 is %i\n", len, len2);
	_printf("Negative:[%d]\n", -762534);
	printf("Negative:[%d]\n", -762534);
	_printf("Unsigned:[%u]\n", ui);
	printf("Unsigned:[%u]\n", ui);
	_printf("Unsigned octal:[%o]\n", ui);
	printf("Unsigned octal:[%o]\n", ui);
	_printf("Unsigned hexadecimal:[%x, %X]\n", ui, ui);
	printf("Unsigned hexadecimal:[%x, %X]\n", ui, ui);
	_printf("Character:[%c]\n", 'H');
	printf("Character:[%c]\n", 'H');
	_printf("String:[%s]\n", "I am a string !");
	printf("String:[%s]\n", "I am a string !");
/*
	_printf("Address:[%p]\n", addr);
	printf("Address:[%p]\n", addr);
*/
	len = _printf("Percent:[%%]\n");
	len2 = printf("Percent:[%%]\n");
	_printf("Len:[%d]\n", len);
	printf("Len:[%d]\n", len2);
/*	_printf("Unknown:[%r]\n");
	printf("Unknown:[%r]\n");
*/	len = _printf("%b\n", 98);
	len = _printf("%b\n", UINT_MAX);
	len2 = printf("11111111111111111111111111111111\n");
	printf("len is %i, len2 is %i\n", len, len2);
	len = _printf("%b, %b\n", 1, 0);
	len = _printf("There is %b bytes in %b KB\n", 1024, 1);
	len2 = printf("There is 10000000000 bytes in 1 KB\n");
	printf("len is %i, len2 is %i\n", len, len2);
	len = _printf("Could you print some non-prntable characters?\n%S\nThanks!\n", "Sure:\x1F\x7F\n");
	len2 = printf("Could you print some non-prntable characters?\nSure:\\x1F\\x7F\\x0A\nThanks!\n");
	printf("len is %i, len2 is %i\n", len, len2);
	p = (void *)0x7fff5100b6f8;
	len = _printf("%pppp\n", p);
	len2 = printf("%pppp\n", p);
	printf("len is %i, len2 is %i\n", len, len2);
	long int l = UINT_MAX;

	l += 1024;
	len = _printf("%b", l);
	len2 = printf("1111111111");
	printf("len is %i, len2 is %i\n", len, len2);

	len = _printf("+ check : %+d", 1024);
	len2 = printf("+ check: %+d", 1024);
	printf("len is %i, len2 is %i\n", len, len2);

	len = _printf("+ check : %+d", -1024);
	len2 = printf("+ check: %+d", -1024);
	printf("len is %i, len2 is %i\n", len, len2);

/*	long int l = INT_MAX;

	l += 1024;
	len = _printf("over INT_MAX %+d", l);
	len2 = printf("over INT_MAX %+d", l);
	printf("len is %i, len2 is %i\n", len, len2);
*/
	len = _printf("# check: %#o", 1024);
	len2 = printf("# check: %#o", 1024);
	printf("len is %i, len2 is %i\n", len, len2);



	return (0);
}
