
# Python selenium test otomasyon projesi

Bu proje Metehan Kart tarafından geliştirilmiştir. Projede kullanılan ve kullanılmayan pytest decorator tagleri aşağıda açıklanmıştır.

# @pytest.fixture

Bu decorator, test fonksiyonlarına veri veya obje sağlamak için kullanılır. Özellikle test fonksiyonları arasında veri veya obje paylaşımını sağlamak için kullanışlıdır. Örneğin testlerden önce chrome driver başlatmak için kullanılabilir.

# @pytest.mark.parametrize

Bu decorator, aynı test fonksiyonunu farklı parametre setleriyle çalıştırmak için kullanılır. Parametrelerle birlikte test fonksiyonu bir dizi kez çalıştırılır ve her bir kombinasyon için ayrı bir test sonucu üretilir. Proje içerisinde listedeki 3 item içinde aynı adımları uygulayan test ile bu parametre kullanıldı.

# @pytest.mark.skip

Bu decorator, bir test fonksiyonunu atlamak için kullanılır. Belirli koşullar altında testin çalıştırılmasını engellemek için kullanılabilir.

# @pytest.mark.skipif

Bu decorator, belirli bir koşul sağlandığında bir testin atlanmasını sağlar.

# @pytest.mark.xfail

Bu decorator, bir testin başarısız olması bekleniyorsa, bu başarısızlığın beklenen bir durum olduğunu belirtmek için kullanılır.