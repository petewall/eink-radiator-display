# eInk Radiator Display

![CI](https://ci.petewall.net/api/v1/teams/main/pipelines/eink-radiator/jobs/test-display/badge)

This project is what displays images to the user interface. It's primarily used for the [Inky wHAT](https://shop.pimoroni.com/products/inky-what?variant=13590497624147) eInk display from [Pimoroni](https://shop.pimoroni.com/).

The code will load the display driver, build a palette of supported colors, and display the image after quantizing it down to the supported color palette.

## Running

```bash
main.py display <path/to/image.png>
```

