
from voxel_parser import VoxParser
from pallete import Pallete

def main():
    pallete_path = "vox//pal0.png"
    voxel_path = "vox//cars.vox"

    pallete =  Pallete(pallete_path)
    pallete.select_pallete()

    voxel_parser = VoxParser(voxel_path)

    voxel_parser.import_vox(pallete)

    for voxel in voxel_parser.voxels:
        print(voxel)
    
    for color in voxel_parser.palette:
        print(color)


if __name__=="__main__":
    main()