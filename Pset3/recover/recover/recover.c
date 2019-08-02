#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Only one argument will be accepted.\n");
        return 1;
    }

    // open memory card
    FILE *memCard = fopen(argv[1], "r");

    if (memCard == NULL)
    {
        printf("No files exist in the memory car.\n");
        return 1;
    }

    // char array for the file name
    char filename[8];

    // files found counter
    int counter = 0;

    //open an empty image file to write to
    FILE *img = NULL;

    unsigned char buffer[512];

    //create a check for jpegs
    bool inJpeg = false;

    // use a while loop to loop through mem card while a block exists
    // read 512 byts blocks at a each loop
    while (fread(buffer, 512, 1, memCard))
    {
        // find begginning of a jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            //close previous jpeg if new one is found, else set inJpeg to true
            if (inJpeg == true)
            {
                fclose(img);
            }
            else
            {
                inJpeg = true;
            }
            //name the file using the counter number
            sprintf(filename, "%03i.jpg", counter);
            // set new image file to the img file
            img = fopen(filename, "w");
            //add to file counter
            counter++;
        }

        if (inJpeg == true)
        {
            // write the code block to img file
            fwrite(&buffer, 512, 1, img);
        }
    }


    fclose(memCard);
    fclose(img);
    return 0;
}
