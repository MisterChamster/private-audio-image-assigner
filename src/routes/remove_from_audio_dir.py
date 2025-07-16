from src.img_to_audio.multiple_audio import remove_images_dir
from src.askers import ask_path_filedialog



def remove_from_audio_dir():
    print("Choose audio directory")
    input_audio_dir_path = ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {input_audio_dir_path}\n")

    remove_images_dir(input_audio_dir_path)
    print("Images succesfully removed\n\n")
