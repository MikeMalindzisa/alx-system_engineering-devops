#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
* infinite_while - a function that runs forever and returns nothing
* Return: 0 in the end
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - the entry point to a program that creates 5 zombie processes
* Return: 0 on success
*/
int main(void)
{
	int baby_zombies = 0;

	pid_t pid;

	/* Create 5 zombie processes */
	while (baby_zombies < 5)
	{
		pid = fork();

		/* Check if it's the child process */
		if (!pid)
			break;

		/* Print a message indicating the creation of a zombie process */
		printf("Zombie process created, PID: %i\n", (int)pid);

		/* Increment the count of created processes */
		baby_zombies++;
	}

	/* Only the parent process runs the infinite_while function */
	if (pid != 0)
		infinite_while();

	return (0);
}

