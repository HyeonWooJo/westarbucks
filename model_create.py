from products.models import *

# Menu create
Menu.objects.create(name = "음료")
Menu.objects.create(name = "푸드")
Menu.objects.create(name = "상품")
Menu.objects.create(name = "카드")

# Category create
Category.objects.create(menu_id = 1, name = "콜드 브루 커피")
Category.objects.create(menu_id = 1, name = "브루드 커피")
Category.objects.create(menu_id = 1, name = "에스프레소")
Category.objects.create(menu_id = 2, name = "브레드")
Category.objects.create(menu_id = 2, name = "케이크")
# Category.objects.create(menu_id = 3, name = "머그")
# Category.objects.create(menu_id = 3, name = "글라스")
# Category.objects.create(menu_id = 4, name = "실물카드")


# Drink create
Drink.objects.create(
    category_id = 1, 
    korean_name = "나이트로 바닐라 크림", 
    english_name = "Nitro Vanilla Cream", 
    description = "부드러운 목넘김의 나이트로 커피와 바닐라 크림의 매력을 한번에 느껴보세요!")

Drink.objects.create(
    category_id = 2, 
    korean_name = "아이스 커피", 
    english_name = "Iced Coffee", 
    description = "깔끔하고 상큼함이 특징인 시원한 아이스 커피!")

Drink.objects.create(
    category_id = 3, 
    korean_name = "카라멜 마키아또", 
    english_name = "Caramel Macchiato", 
    description = "향긋한 바닐라 시럽과 따뜻한 스팀 밀크 위에 풍성한 우유 거품을 얹고 점을 찍듯이 에스프레소를 부은 후 벌집 모양으로 카라멜 드리즐을 올린 달콤한 커피 음료")

Drink.objects.create(
    category_id = 4, 
    korean_name = "리얼 블루베리 베이글", 
    english_name = "Blueberry Bagel", 
    description = "블루베리의 상큼한 풍미가 매력적인 베이글로 국내산 감자, 보리가루를 넣어 더욱 촉촉하고 건강하게 만들었습니다.")

Drink.objects.create(
    category_id = 5, 
    korean_name = "라즈베리 쇼콜라", 
    english_name = "Raspberry chocolate Cake", 
    description = "초콜릿 케이크 사이에 진한 가나슈 필링을 넣은 후 라즈베리를 올린 진하고 묵직한 초콜릿 케이크입니다.")

# Drink.objects.create(
#     category_id = 6, 
#     korean_name = "SS 블랙 데비 머그 414ml", 
#     english_name = "SS black debbie mug 414ml", 
#     description = "우아함과 기품이 느껴지는 블랙 컬러를 배색하여 계절과 성별에 구애받지 않고 사용할 수 있는 심플한 디자인의 414ml 스테인리스 머그입니다.")

# Drink.objects.create(
#     category_id = 7, 
#     korean_name = "티바나 더블월 글라스 355ml", 
#     english_name = "Teavana double wall glass 355ml", 
#     description = "Teavana bar 매장 전용 상품")

# Drink.objects.create(
#     category_id = 8, 
#     korean_name = "더북한강R 스타벅스 카드", 
#     english_name = "The Bukhangang R Starbucks Card", 
#     description = "없음")


# Allergy Create
Allergy.objects.create(name = "대두")
Allergy.objects.create(name = "우유")
Allergy.objects.create(name = "난류")
Allergy.objects.create(name = "밀")
Allergy.objects.create(name = "아황산류")
Allergy.objects.create(name = "토마토")


# Allergy_Drink Create
Allergy_Drink.objects.create(allergy_id = 2, drink_id = 1)
Allergy_Drink.objects.create(allergy_id = 1, drink_id = 3)
Allergy_Drink.objects.create(allergy_id = 2, drink_id = 3)
Allergy_Drink.objects.create(allergy_id = 4, drink_id = 4)
Allergy_Drink.objects.create(allergy_id = 1, drink_id = 5)
Allergy_Drink.objects.create(allergy_id = 2, drink_id = 5)
Allergy_Drink.objects.create(allergy_id = 3, drink_id = 5)
Allergy_Drink.objects.create(allergy_id = 4, drink_id = 5)
Allergy_Drink.objects.create(allergy_id = 5, drink_id = 5)


# Image Create
Image.objects.create(image_url = "https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[9200000002487]_20210426091745609.jpg", drink_id = 1)
Image.objects.create(image_url = "https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[106509]_20210430111852999.jpg", drink_id = 2)
Image.objects.create(image_url = "https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[126197]_20210415154610012.jpg", drink_id = 3)
Image.objects.create(image_url = "https://image.istarbucks.co.kr/upload/store/skuimg/2021/03/[9300000003334]_20210310092057568.jpg", drink_id = 4)
Image.objects.create(image_url = "https://image.istarbucks.co.kr/upload/store/skuimg/2021/03/[9300000002929]_20210325161742703.jpg", drink_id = 5)


# Size Create
Size.objects.create(name="Tall(톨)", size_ml="355ml", size_fluid_ounce="12 fl oz")
Size.objects.create(name="Grande(그란데)", size_ml="473ml", size_fluid_ounce="16 fl oz")
Size.objects.create(name="Venti(벤티)", size_ml="591ml", size_fluid_ounce="20 fl oz")
# Size.objects.create(name="없음", size_ml="없음", size_fluid_ounce="없음")


# Nutrition Create
Nutrition.objects.create(
    one_serving_kcal = 80,
    sodium_mg = 40,
    saturated_fat_g = 2,
    sugars_g = 10,
    protein_g = 1,
    caffeine_mg = 232,
    drink_id = 1,
    size_id = 1
)

Nutrition.objects.create(
    one_serving_kcal = 5,
    sodium_mg = 10,
    saturated_fat_g = 0,
    sugars_g = 0,
    protein_g = 0,
    caffeine_mg = 140,
    drink_id = 2,
    size_id = 1
)

Nutrition.objects.create(
    one_serving_kcal = 200,
    sodium_mg = 130,
    saturated_fat_g = 5,
    sugars_g = 22,
    protein_g = 88,
    caffeine_mg = 75,
    drink_id = 3
)

Nutrition.objects.create(
    one_serving_kcal = 261,
    sodium_mg = 574,
    saturated_fat_g = 0.3,
    sugars_g =7 ,
    protein_g = 10,
    caffeine_mg = 0,
    drink_id = 4
)

Nutrition.objects.create(
    one_serving_kcal = 535,
    sodium_mg = 95,
    saturated_fat_g = 12,
    sugars_g = 41,
    protein_g = 6,
    caffeine_mg = 0,
    drink_id = 5
)

