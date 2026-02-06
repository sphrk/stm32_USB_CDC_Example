#ifndef __INC_USB_SERIAL__
#define __INC_USB_SERIAL__

#include "main.h"
#include "usbd_cdc_if.h"

#define USB_FIFO_SIZE 	1000

void USB_write_fifo(uint8_t *data, uint16_t len);
uint16_t USB_get_fifo_count(void);
uint8_t USB_Read(uint8_t *data, uint16_t data_len);
uint8_t USB_Write(uint8_t *data, uint16_t len);

#endif
