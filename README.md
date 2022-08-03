# Python-voxel-parser

Para obter informaçãoes de um ficheiro voxel (vox)

## Como usar 

Cada voxel tem uma paleta de cores que é uma imagem de 256 pixel de largura e 1 pixel de altura ,por vezes as informações de cor podem estar no arquivo vox
mas é necessário sempre disponibilizar a paleta , caso o seu modelo não tenha uma paleta você pode gerar um usando o software [MagicaVoxel](https://ephtracy.github.io/)
<div>
Paleta padrão do MagicaVoxel <br>
<img src="vox/pal0.png"> <br>
<br>
</div>

>`````
>pallete_path = "vox//pal0.png"
>pallete =  Pallete(pallete_path)
>`````

Em vez de indicar a paleta você também pode selecionar 

>`````
>pallete =  Pallete("")
>pallete.select_pallete()
>`````
Selecione o arquivo voxel a ser analisado
>`````
>voxel_path = "vox//cars.vox"
>voxel_parser = VoxParser(voxel_path)
>`````
Para importar analisar o vox , e nesse momento que deve disponibilizar a paleta usada
>`````
>voxel_parser.import_vox(pallete)
>`````

Para acessar os dados 
>`````
>voxel_parser.voxels
>voxel_parser.palette
>`````
