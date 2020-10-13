import datetime
import threading
import time

import cv2
import numpy as np

from .system import System


class Record(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name="record_thread")
        system = System()
        json_loads = system.json_loads()
        self._camera_cap = cv2.VideoCapture("rtsp://admin:Dvr12345@192.168.10.101:554/cam/realmonitor?channel=4&subtype=0")
        self._width = int(self._camera_cap.get(3))
        self._height = int(self._camera_cap.get(4))
        self._sec = "SECTRANS"
        self._company = json_loads["record"]["company"]
        self._car = json_loads["record"]["car"]
        self._camera = json_loads["record"]["cam_id"]
        self._cam_flip = json_loads["record"]["cam_flip"]
        self._video_path = json_loads["record"]["video_path"]
        self._video_name = json_loads["record"]["video_name"]
        self._framerate = json_loads["record"]["framerate"]
        self._duration = json_loads["record"]["duration"] + 1

    def video_capture(self):
        """Método responsável por realizar a captura de vídeos.
        """

        print('Iniciando video_capture')
        try:
            system = System()
            video_name = str(datetime.datetime.now().strftime(self._video_name))
            video_path = system.create_dir(self._video_path)
            video_output = f"{self._video_path}/{video_name}"
            width = self._width
            height = self._height
            framerate = self._framerate

            time_start = time.time()

            print('Iniciando gravação')
            out = cv2.VideoWriter(video_output, cv2.VideoWriter_fourcc(*"mp4v"), framerate, (width, height))

            while True:
                # Para cada frame capturado é inserido informações 
                ret, frame = self._camera_cap.read()

                if ret == True:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    sec = self._sec
                    date_time = str(
                        datetime.datetime.now().strftime("DIA: %d/%m/%Y - HORA: %T")
                    )
                    company = str(self._company).upper()
                    car = self._car
                    v_camera = self._camera
                    vehicle = f"CARRO: {car}({v_camera})"

                    # inseri tarja superior e inferior no vídeo além das informações
                    #  sobre de data e hora, nome da empresa e nome do cliente

                    print('colocando texto')
                    frame = img = cv2.rectangle(frame, (0, 0), (width, 20), (0, 0, 0), -1)
                    frame = img2 = cv2.rectangle(frame, (0, height + 30), (width, height - 20), (0, 0, 0), -1)
                    frame = cv2.putText(frame, company, (5, 15), font, 0.4, (0, 255, 255), 1, cv2.LINE_AA)
                    frame = cv2.putText(frame, sec, (635, 15), font, 0.4, (0, 255, 255), 1, cv2.LINE_AA)
                    frame = cv2.putText(frame, vehicle, (5, 475), font, 0.4, (0, 255, 255), 1, cv2.LINE_AA,)
                    frame = cv2.putText(frame, date_time, (465, 475), font, 0.4, (0, 255, 255), 1, cv2.LINE_AA,)

                    print('gravando texto')
                    out.write(frame)

                    # tempo de duração do vídeo
                    print(f'verificando tempo {time.time() - time_start} {float(self._duration)}')
                    current_time = time.time() - time_start
                    print(type(current_time))
                    print(type(self._duration))

                    if current_time >= float(self._duration):
                        print(f"Vídeo gravado em: {video_output}")
                        break
                else:
                    break

            print('finalizando')
            self._camera_cap.release()
            out.release()
            cv2.destroyAllWindows()

        # except AttributeError:
        #     pass
        except Exception as e:
            print(f"Erro record: {e}")
        finally:
            return False

    def run(self):
        """[Sobrecarga do método run]

        To do: trocar print por log no sistema
        """

        try:
            print("Iniciando Gravação")
            self.video_capture()
            print("Concluindo Gravação")
        except Exception as e:
            print(f'Erro: {e}')
        
