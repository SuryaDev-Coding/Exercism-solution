#include "grains.h"
uint64_t square(uint8_t index){
    if(index<=0||index>64){
        return 0;
    }
    uint64_t number = 1UL <<(index-1);
    return number;
}
uint64_t total(void){
    uint64_t sum = (((1ULL<<63)-1)<< 1)+1;
    //1ul<<64 = 10000...0 followed by 63 zeroes, 1 in 64th position.
    //(1ul<<64)-1 = 01111...1  63 ones, start zero
    //((1ul<<64)-1)<<1 = 111...0 63 ones, end zero
    //(((1ULL<<63)-1)<< 1)+1 = 1111...1 64 ones, final is flipped.
    return sum ;
}