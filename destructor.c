/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   destructor.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mfunyu <mfunyu@student.42tokyo.jp>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/09/01 21:22:15 by mfunyu            #+#    #+#             */
/*   Updated: 2021/09/01 21:33:12 by mfunyu           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define RED "\033[31m"
#define GREEN "\033[32m"
#define RESET "\033[0m"

void	leak_checker(void)__attribute__((destructor));

void	leak_checker(void)
{
	int		status;

	status = system("leaks philo > ./tests/logs/leak_log");
	if (WIFEXITED(status) && WEXITSTATUS(status) == 0)
	{
		system("grep -C2 malloced ./tests/logs/leak_log");
		fprintf(stderr, "%sOK! No memory leaks :)%s\n", GREEN, RESET);
	}
	else
	{
		system("grep TOTAL -A 10 ./tests/logs/leak_log");
		fprintf(stderr, "%sKO! Memory leak detected :(%s\n", RED, RESET);
	}
}
