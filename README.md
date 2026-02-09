# stm32_USB_CDC_Example

Transmitting and Receiving Data with STM32 USB Peripheral.
- Transmitting data with CDC_Transmit_FS.
- Receiving data by changing CDC_Receive_FS callback (copy received bytes to temporary buffer).
- Processing received data with FIFO (adding received data to FIFO buffer in CDC_Receive_FS callback, and in main.c in while loop, reading received data from FIFO).

### Implemented examples:
- if 0x55 received, send "Hello world".
- if 0x01 received, add two next received values and send result.
- if 0xAA received, increment next received value and  send result.
