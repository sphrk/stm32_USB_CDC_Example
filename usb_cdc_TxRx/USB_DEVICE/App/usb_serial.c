#include "usb_serial.h"

typedef struct{
	uint16_t read_index;
	uint16_t write_index;
	uint8_t fifo[USB_FIFO_SIZE];
}usb_fifo_t;

usb_fifo_t usb_fifo = {
	.read_index = 0,
	.write_index = 0
};

void USB_write_fifo(uint8_t *data, uint16_t len){
	int i;
	for(i=0; i<len; i++){
		usb_fifo.fifo[usb_fifo.write_index++] = data[i];
		if(usb_fifo.write_index >= USB_FIFO_SIZE){
			usb_fifo.write_index = 0;
		}
	}
}

uint16_t USB_get_fifo_count(void){
	if(usb_fifo.write_index >= usb_fifo.read_index){
		return usb_fifo.write_index - usb_fifo.read_index;
	}
	return USB_FIFO_SIZE - usb_fifo.read_index + usb_fifo.write_index;
}

uint8_t USB_Read(uint8_t *data, uint16_t data_len){
	if(USB_get_fifo_count() < data_len)
		return 0;
	/* Read From FIFO */
	int i;
	for(i=0; i<data_len; i++){
		data[i] = usb_fifo.fifo[usb_fifo.read_index++];
		if(usb_fifo.read_index >= USB_FIFO_SIZE){
			usb_fifo.read_index = 0;
		}
	}
	return 1;
}

uint8_t USB_Write(uint8_t *data, uint16_t len){
	while(USBD_BUSY == CDC_Transmit_FS(data, len)){};
	return 1;
}


