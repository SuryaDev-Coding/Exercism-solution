#include "difference_of_squares.h"
unsigned int sum_of_squares(unsigned int number){
    unsigned int sum_square;
    sum_square = ((number) * (number+1) * (2*number+1))/6;
    return sum_square;
}

unsigned int square_of_sum(unsigned int number){
    unsigned int square_sum;
    square_sum = ((number*(number+1))/2)*((number*(number+1))/2);
    return square_sum;
}

unsigned int difference_of_squares(unsigned int number){
    unsigned int sum_square, square_sum, difference_square;
    sum_square= sum_of_squares(number);
    square_sum= square_of_sum(number);
    difference_square = square_sum - sum_square;
    return difference_square;
}