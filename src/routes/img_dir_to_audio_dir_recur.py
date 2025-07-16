
from src.img_to_audio.recurring_classes.embed_recursive_conditional import Embed_Recursive_Conditional
from src.askers import ask_path_filedialog



def img_dir_to_audio_dir_recur():
    print("Choose image directory")
    input_image_dir_path = ask_path_filedialog("d", "Image directory path")
    print(f"Path chosen: {input_image_dir_path}\n")
    print("Choose audio directory")
    input_audio_dir_path = ask_path_filedialog("d", "Audio directory path")
    print(f"Path chosen: {input_audio_dir_path}\n")

    # recurrer_cond = Embed_Recursive(input_image_dir_path)
    # recurrer_cond.embed_images_recursion(input_audio_dir_path)
    recurrer_cond = Embed_Recursive_Conditional(input_image_dir_path)
    recurrer_cond.embed_images_recursion_conditional(input_audio_dir_path)
