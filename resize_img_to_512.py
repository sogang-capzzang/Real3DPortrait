from PIL import Image

def resize_image(input_path, output_path, size=(512, 512)):
    """
    이미지 파일을 지정된 크기로 리사이즈한 후 저장합니다.
    
    Args:
        input_path (str): 원본 이미지 경로
        output_path (str): 저장할 리사이즈된 이미지 경로
        size (tuple): 리사이즈 크기 (가로, 세로)
    """
    try:
        # 이미지 열기
        img = Image.open(input_path)

        # 이미지 리사이즈
        resized_img = img.resize(size, Image.LANCZOS)

        # 이미지 저장
        resized_img.save(output_path)

        print(f"이미지가 성공적으로 저장되었습니다: {output_path}")
    except Exception as e:
        print(f"이미지 처리 중 오류 발생: {e}")

if __name__ == "__main__":
    # input 이미지 
    input_file = "./crop2.png"
    # output 이미지 파일명
    output_file = "resized_512x512_FEM40_3.png"
    
    resize_image(input_file, output_file)
