
from voxel_parser import VoxParser

def main():
    path = "shiba2.vox"

    voxel_data = VoxParser(path)
    print(voxel_data.palette)
    print(voxel_data.voxels)
    print(voxel_data.size)


if __name__=="__main__":
    main()