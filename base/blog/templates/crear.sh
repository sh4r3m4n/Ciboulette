#!/bin/bash

ls contenido/ | while read i;do
	cat maqueta/header.html contenido/$i maqueta/footer.html > $i
done
