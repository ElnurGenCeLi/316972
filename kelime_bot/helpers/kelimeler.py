import random
kelimeler = [ 'səy', 'hər gün', 'ekspress', 'risk', 'danışma', 'söz', 'demokratiya', 'duz', 'məscid', 'yaş', 'aşağı',
             'ətrafında', 'tezliklə', 'imkan', 'orqan', 'öldürmək', 'başqa', 'il', 'çürümək', 'baxmaq', 'meyvə', 'asmaq',
             'şirin', 'ayaq', 'dəyişiklik', 'qanun', 'külək', 'respublika', 'təkmilləşmək', 'üslub', 'yeddi', 'azalmaq',
             'qoşulmaq', 'mobil telefon', 'əlaqə', 'menecer', 'otel', 'qaçmaq', 'zövq almaq', 'sürüş', 'təhlükəsizlik', 'qanun',
             'et', 'modern', 'oxumaq', 'tüfəng', 'tələb', 'ulduz', 'intensiv', 'əsgər', 'sadə', 'adlanacaq', 'qaz',
             'tətbiq', 'istehsal', 'bəyannamə', 'yemək', 'dünən', 'bax', 'haqqında', 'alış-veriş', 'şüur', 'çərçivə',
             'lazımdır', 'mövcuddur', 'istehlakçı', 'uzatmaq', 'to', 'at', 'qoşulmaq', 'məsələn', 'demək olar', 'sayt',
             'kömək', 'bacı', 'çiçək', 'hamısı', 'hörmət', 'ödəmək', 'istedad', 'ağırlıq', 'pay', 'çətin', 'bundan başqa',
             'çay', 'gedər', 'əmin', 'zəngin', 'heç vaxt', 'söz', 'təşkilat', 'ticarət', 'make out', 'boyun', 'cihaz',
             'balans', 'gedəcək', 'geri', 'qəhvə', 'əzələ', 'montaj', 'başqa', 'işlə məşğul olmaq', 'ünvan', 'müəyyən etmək',
             'paşa', 'istilik', 'yaxşı', 'güvən', 'marka', 'yarpaq', 'fayda', 'yaymaq', 'axan', 'çəkmək', 'düşünmək',
             'ürək', 'arzu', 'tərəqqi', 'şərab', 'yuxarıda', 'qızıl', 'arandırmaq', 'almaq', 'təqdim etmək', 'təmiz',
             'vitamin', 'əlavə', 'gec', 'aktyor', 'yumurta', 'həddindən artıq', 'hərəkət', 'istəyək', 'kəsmə', 'böhran', 'vahid',
             'söndür' , 'yarım', 'yetər', 'fərdi', 'qaranlıq', 'avtobus', 'sənaye', 'körpə', 'vətəndaş', 'nazir', 'zaman', 'millət',
             'reklam', 'yüksəlmə', 'ölçü', 'jurnal', 'inflyasiya', 'sosial', 'kimsə', 'keçmiş', 'xəstəxana', 'varlıq',
             'görüş', 'jurnalist', 'daxili', 'inam', 'keyfiyyət', 'bitdi', 'bitiş', 'yerləşin', 'giriş', 'rahat',
             'cəmi', 'birlikdə', 'gizli', 'oxşar', 'dəri', 'çevirmək', 'döyüş', 'problem', 'xidmət', 'müalicə',
             'yaşıl', 'nazirlik', 'təzyiq', 'reaksiya', 'cümlə', 'istək', 'azadlıq', 'yenidən', 'şəxsiyyət', 'məsələ', 'üçüncü',
             'müəyyən et', 'qiymətləndirmək', 'maraqlı', 'sürücü', 'süd', 'tutmaq', 'eşya', 'beynəlxalq', 'namizəd',
             'çəki', 'milyard', 'sağlam', 'sıxıntı', 'tanrı', 'rəftar', 'sosial', 'nəşriyyat', 'diqqətli', 'son dərəcə',
             'topla', 'investisiya et', 'işıqlandırmaq', 'qarışdırmaq', 'təhlükə', 'zaman', 'dairə', 'imkan', 'proses', 'qarışdırmaq',
             'töhfə', 'hekayə', 'tamamilə', 'təyyarə', 'cavab', 'təbiət', 'evlənmək', 'burun', 'faiz', 'əlbəttə', 'işçi', 'iş',
             'qısaca', 'mağaza', 'media', 'çünki', 'artım', 'çıxarmaq', 'ictimai', 'sığorta', 'yay', 'ürək', 'sənəd',
             ]


def kelime_sec():
    return random.choice(kelimeler)
