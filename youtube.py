# 機械学習・ディープラーニング系では必須のライブラリ（データ処理を最適化してくれているイメージ）
import pandas as pd
 
#youtubeデータをpandasに変換する関数
def get_video_info(part, q, order, type, num):
    dic_list = []
    search_response = youtube.search().list(part=part,q=q,order=order,type=type)
    output = youtube.search().list(part=part,q=q,order=order,type=type).execute()

    #デフォルトでは5件しか取得できないので、繰り返し取得
    for i in range(num):        
        dic_list = dic_list + output['items']
        search_response = youtube.search().list_next(search_response, output)
        output = search_response.execute()

    df = pd.DataFrame(dic_list)
    #各動画毎に一意のvideoIdを取得
    df1 = pd.DataFrame(list(df['id']))['videoId']
    #各動画毎に一意のvideoIdを取得必要な動画情報だけ取得
    df2 = pd.DataFrame(list(df['snippet']))[['channelTitle','publishedAt','channelId','title','description']]
    ddf = pd.concat([df1,df2], axis = 1)

    return ddf

#キーワード筋トレでデータを20回×5件取得
df_out = get_video_info(part='snippet',q='美容系youtuber',order='viewCount',type='video',num = 20)
df_out