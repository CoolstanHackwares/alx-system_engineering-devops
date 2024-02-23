#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - A function that runs an infinite loop.
 *
 * This function creates an infinite loop using sleep(1).
 *
 * Return: Always returns 0.
 * This program conforms to the betty documentation styles
 **/

int infinite_while(void)
{
	while (1)
{
	sleep(1);
}
	return (0);
}

/**
 * main - Entry point of the program.
 *
 * A function that creates 5 zombie processes and prints the PID
 * of each zombie process.
 *
 * Return: Always returns 0.
 * This program conforms to the betty documentation style
 **/

int main(void)
{
	int a;

	for (a = 0; a < 5; a++)
{
	pid_t pid = fork();

	if (pid > 0)
{
	/* Parent process */
	printf("Zombie process created, PID: %d\n", pid);
}
	else if (pid == 0)
{
	/* Child process */
	exit(0);
}
	else
{
	/* Error handling if fork fails */
	perror("fork");
	exit(EXIT_FAILURE);
}
}
	/* Infinite loop to keep the program running */
	infinite_while();

	return (0);
}
