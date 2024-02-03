import subprocess

class ScreenRecorder:
    def __init__(self):
        self.recording_process = None

    def start_recording(self, output_file='screen_recording.mp4'):
        """
        화면 녹화를 시작합니다.
        :param output_file: 녹화된 파일이 저장될 경로
        """
        # macOS의 화면을 캡처하기 위해 avfoundation과 함께 캡처할 화면 인덱스 '1'을 사용합니다.
        # 추가 옵션은 필요에 따라 조정할 수 있습니다.
        command = [
            'ffmpeg',
            '-f', 'avfoundation',
            '-i', '1:0',  # '1'은 화면, '0'은 오디오 장치. 오디오가 필요 없다면 '1:'로 설정
            '-r', '30',  # 초당 프레임 수
            '-s', '1920x1080',  # 해상도
            '-vcodec', 'libx264',  # 비디오 코덱
            '-crf', '28',  # 비디오 품질, 값이 낮을수록 품질이 좋음
            '-pix_fmt', 'yuv420p',  # 픽셀 포맷
            output_file
        ]
        self.recording_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    def stop_recording(self):
        """
        화면 녹화를 중지합니다.
        """
        if self.recording_process:
            # ffmpeg 프로세스에 'q' 문자를 보내어 안전하게 녹화를 종료합니다.
            self.recording_process.communicate(input=b'q')
            self.recording_process = None

if __name__ == "__main__":
    recorder = ScreenRecorder()
    recorder.start_recording('my_screen_recording.mp4')  # 녹화 시작
    input("Press Enter to stop recording...")  # 사용자 입력을 기다립니다.
    recorder.stop_recording()  # 녹화 종료
