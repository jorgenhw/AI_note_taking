import os
from src.functions import import_whisper, set_api_key, keep_full_length, shorten_with_gpt, main_points_with_gpt, change_tone_elim5, restructure_gpt3
import argparse

def main(args):

    ################################
    # Loading the audio file #######
    audio_file_path = os.path.join("audio_files", "Sample_file.mp3")
    ################################
    ################################

    # Transcribing text using whisper
    text = import_whisper(audio_file_path, model_name=args.model_name) # model_name="small"
    
    # Get the API's key from the .env file
    set_api_key()
    
    # get the shortened version of the text
    shortened_text = shorten_with_gpt(text)
    # make output directory if it is not already there
    if not os.path.exists("output"):
        os.mkdir("output")
    # save the shortened text to a file in a folder called output
    with open("output/shortened_text.txt", "w") as f:
        f.write(shortened_text)
    
    # get the main points of the text
    main_points = main_points_with_gpt(text)
    with open("output/main_points.txt", "w") as f:
        f.write(main_points)

    # get the text explained like I'm 5
    explained_like_im_5 = change_tone_elim5(text)
    with open("output/explained_like_im_5.txt", "w") as f:
        f.write(explained_like_im_5)
    
    # get the full length version of the text
    full_length_text = keep_full_length(text)
    with open("output/full_length_text.txt", "w") as f:
        f.write(full_length_text)

    # get the restructured text
    restructured_text = restructure_gpt3(text)
    with open("output/restructured_text.txt", "w") as f:
        f.write(restructured_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Speech to text to notes')
    parser.add_argument('--model_name', type=str, default="small", help='specify which whisper model to use (tiny, base, small, medium, large)')
    args = parser.parse_args()
    main(args)