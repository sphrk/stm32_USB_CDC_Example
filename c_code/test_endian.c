#include <stdio.h>
#include "inttypes.h"

int main(){
    // uint16_t a = 0xABCD;

    // int i;
    // for(i=0; i<2; i++){
    //     printf("%X\n", ((uint8_t *)&a)[i]);
    // }
    /* ################################################## */

    // uint16_t a = 0xABCD;
    
    // uint8_t *ptr = (uint8_t *)&a;

    // int i;
    // for(i=0; i<2; i++){
    //     printf("%X\n", ptr[i]);
    // }
    /* ################################################## */

    // uint32_t b = 0x1A2B3C4D;

    // int i;
    // for(i=0; i<4; i++){
    //     printf("%X\n", ((uint8_t *)&b)[i]);
    // }

    /* ################################################## */

    // uint32_t c[3] = {0x1A2B3C4D, 0x12345678, 0x11223344};

    // int i;
    // for(i=0; i<4*3; i++){
    //     printf("%X\n", ((uint8_t *)c)[i]);
    // }

    /* ################################################## */
    // uint32_t c[3] = {0x1A2B3C4D, 0x12345678, 0x11223344};

    // uint32_t *ptr32 = c;
    // uint8_t *ptr = (uint8_t *)ptr32;

    // int i;
    // for(i=0; i<4*3; i++){
    //     printf("ptr[%d] = %X\n", i, ptr[i]);
    // }

    /* ################################################## */
    uint8_t f[4] = {0xAB, 0x12, 0xBC, 0x34};

    uint16_t *g = (uint16_t *)f;
    printf("g[0] = 0x%X\n", g[0]);
    printf("g[1] = 0x%X\n", g[1]);

    uint32_t *h = (uint32_t *)f;
    printf("h = 0x%X\n", *h);

    uint32_t k = *((uint32_t *)f);
    printf("k = 0x%X\n", k);



    return 0;
}


