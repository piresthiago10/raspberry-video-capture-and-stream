import json
import os

class System():

    def create_dir(self, video_path):
        """[Método responsável por criar diretório de gravação de vídeo
        caso não exista]

        Args:
            video_path ([string]): [diretório de gravação do video]

        Returns:
            [string]: [caminho de gravação de vídeo]
        """

        video_path = os.path.join(video_path)
        if os.path.isdir(video_path):
            pass
        else:
            os.makedirs(video_path)
            # descomentar quanto estiver no rodando no supervisor
            # os.system("chmod -R 777" + video_path)
            return video_path


    def json_loads(self):

        try:
            with open('./docs/config.json', 'r') as data:
                data = json.load(data)
                return data
        except Exception as e:
            return print(e)