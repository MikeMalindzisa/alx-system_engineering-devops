#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * main - creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();

		if (!zombie)

			exit(0);

		printf("Zombie process created, PID: %d\n", getpid());
	}
	while (1)
		sleep(1);

	return (0);
}
