import yt_dlp

def baixar_video(url):
    try:
        ydl_opts = {
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
            'merge_output_format': 'mp4',
            'postprocessors': [
                {
                    'key': 'FFmpegVideoConvertor',  # Converte para MP4 corretamente
                    'preferedformat': 'mp4',
                },
                {
                    'key': 'FFmpegMetadata',  # Corrige metadados do arquivo
                }
            ],
            'noplaylist': True,
            'cookiefile': 'cookies.txt',  # Para login no Instagram/Facebook
            'quiet': False,  # Exibe logs
            'ignoreerrors': True,  # Evita falhas ao encontrar erros menores
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print('✅ Download do vídeo concluído com sucesso!')
    except Exception as e:
        print(f'❌ Ocorreu um erro ao baixar o vídeo: {e}')

if __name__ == "__main__":
    url_video = input('Digite a URL do vídeo: ')
    baixar_video(url_video)