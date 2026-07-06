#include "grains.h"
#include<math.h>
uint64_t square(uint8_t index){
    if(index<=0||index>64){
        return 0;
    }
    uint64_t number = 1UL <<(index-1);
    return number;
}
uint64_t total(void){
    uint64_t sum = ((1ULL<<63)<<1)-1;
    return sum ;
}