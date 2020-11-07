# Amazon Scraper

Flask API to get JSON data about Amazon Products

Selectorlib selector based on tutorial at [ScrapeHero Tutorials](https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python-and-selectorlib/)

## Features
1. Cached(prevents redundancy & also prevents being rate-limited & increases speed)
2. Search
3. Product Details
4. Rotates User Agent Strings(prevents being rate-limited)

## Installation

From a terminal 

1. Clone this project and cd into it `cd amazon-scraper`
2. Add a Virtual Environment `python3 -m venv .venv` (Optional)
3. Activate the Virtual Environment `source .venv/bin/activate` (Optional) 
4. Install Requirements `pip3 install -r requirements.txt`

### Usage
Run
```sh
python main.py
```

### GET /product/<id>
  example: http://127.0.0.1:8080/product/B0863N5FM8
```json
{
  "name": "2020 Premium HP 15 Laptop Computer PC, 15.6 inch HD Touchscreen, 8th Gen Intel Dual-Core i3 8145U (>i5-7200U), 4GB DDR4 512GB SSD, WiFi BT 4.2 USB-C HDMI Win 10 S (Silver) + Delca 16GB Micro SD Card",
  "price": "$679.00",
  "short_description": "About this item This fits your . Make sure this fits by entering your model number. P.when(\"ReplacementPartsBulletLoader\").execute(function(module){ module.initializeDPX(); }) \\u3010HP i3-8145U Laptop \\u3011: The Powerful and Fast 8th Generation Intel Core i3 Processors, Intel Dual-Core i3-8145U (>i5-7200U), 2.1 GHz base frequency, up to 3.9 GHz with Intel Turbo Boost Technology, 4 MB Intel Smart Cache, 4 Treads \\u3010Upgraded Powerful Storage\\u3011: 4GB DDR4 SDRAM Memory, 512GB Solid State Drive \\u3010hp 15.6 touchscreen laptop\\u3011: 15.6-inch HD (1366 x 768) Touchscreen Micro-Edge\\u00a0Widescreen LED Display; Integrated Intel UHD Graphics 620 \\u3010External Ports and Slots\\u3011: 1 x USB 3.1 Gen 1 Type-C (Data Transfer Only, 5 Gb/s signaling rate), 2 x USB 3.1 Gen 1 (Data transfer only), 1 x AC smart pin, 1 x HDMI, 1 x RJ-45, 1 x headphone/microphone combo, 1 x multi-format SD media card reader \\u3010Operating System\\u3011 : Windows 10 in S mode is designed for security and performance. If you want to switch out of S mode, please follow the link: https://support.microsoft.com/en-us/help/4456067/windows-10-switch-out-of-s-mode. HP TrueVision HD Camera with integrated dual array digital microphone, Realtek RTL8821CE 802.11b/g/n/ac (1x1) Wi-Fi and Bluetooth 4.2 Combo, up to 10.5 hours battery life, Accessory Including a Delca 16GB Micro SD Card \\u009b See more product details",
  "images": "{\"https://images-na.ssl-images-amazon.com/images/I/41lfhgOHQEL._AC_SX466_.jpg\":[324,466],\"https://images-na.ssl-images-amazon.com/images/I/41lfhgOHQEL._AC_SX355_.jpg\":[247,355],\"https://images-na.ssl-images-amazon.com/images/I/41lfhgOHQEL._AC_.jpg\":[348,500],\"https://images-na.ssl-images-amazon.com/images/I/41lfhgOHQEL._AC_SX450_.jpg\":[313,450],\"https://images-na.ssl-images-amazon.com/images/I/41lfhgOHQEL._AC_SX425_.jpg\":[296,425]}",
  "rating": null,
  "number_of_reviews": null,
  "variants": null,
  "product_description": "Capacity: 4GB DDR4 I 512GB SSD |\\u00a0\n\nColor: Silver This listing by Apricot\\u00a0Power\\u00a0PC\\u00a0sells\\u00a0computers\\u00a0with\\u00a0upgraded configurations.If the computer has modifications (listed above), then the manufacturer box is opened for it to be tested and inspected and to install the upgrades to achieve the specifications as advertised. If no modification are listed, the item is unopened and untested. Defects & blemishes are significantly reduced by our in depth inspection & testing PRODUCT OVERVIEW: Stay connected to what matters most with long-lasting battery life and a sleek and portable, micro-edge bezel design with the HP 15.6\\u201d Touchscreen Laptop. Built to keep you productive and entertained from anywhere, the HP 15-inch laptop features reliable performance and an expansive display - letting you stream, surf and speed through tasks from sun up to sun down. KEY SPECIFICATIONS: PC Type: Traditional Notebook Laptop Computer PC Series: HP 15.6 i3 Display: 15.6-inch HD (1366 x 768) Touchscreen Micro-Edge Display Processor: Intel Dual-Core i3-8145U (>i5-7200U), 2.1 GHz up to 3.9GHz, 4 MB Intel Smart Cache, 4 Threads Memory: 4GB DDR4 SSD: 512GB Solid State Drive Graphics: Integrated Intel UHD Graphics 620 Communications: 802.11ac and Bluetooth 4.2 Camera: Built-in HD Webcam Operating system: Windows 10 Ports & Slots: 1 x USB 3.1 Gen 1 Type-C , 2 x USB 3.1 Gen 1, 1 x AC smart pin, 1 x HDMI, 1 x RJ-45, 1 x headphone/microphone combo, 1 x multi-format SD media card reader Additional Information: Dimensions: 14.11\" x 9.53\" x 0.78\" Approximate Weight: 3.84lbs Color: Silver Accessory: DELCA\\u00a016GB\\u00a0Microso\\u00a0SD\\u00a0included",
  "sales_rank": null,
  "link_to_all_reviews": "/HP-15-Computer-Touchscreen-Dual-Core/product-reviews/B0863N6KD9/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
}
```

### GET /search/<query> 
  example: http://127.0.0.1:8080/search/pikachu

```json
{
  "products": [
    {
      "title": "Pok\\u00e9mon Pikachu Plush Stuffed Animal - Winking - Large 12\"",
      "url": "/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A0027644XALA8UOXZ93K&url=%2FPoK%25C3%25A9MoN-Winking-Pikachu-Stuffed-Animal%2Fdp%2FB07SPGG292%2Fref%3Dsr_1_1_sspa%3Fdchild%3D1%26keywords%3Dpikachu%26sr%3D8-1-spons%26psc%3D1&qualifier=1604683213&id=1937612254046914&widgetName=sp_atf",
      "rating": "4.8 out of 5 stars",
      "reviews": "275",
      "price": "$18.99"
    },
    {
      "title": "Pok\\u00e9mon 8\" Plush - Pikachu",
      "url": "/Pok%C3%A9mon-Official-Premium-Quality-Plush/dp/B07RBBCZZ1/ref=sr_1_6?dchild=1&keywords=pikachu&sr=8-6",
      "rating": "4.8 out of 5 stars",
      "reviews": "1,525",
      "price": "$12.98"
    },
    {
      "title": "3D crystal LED Night Light,7 Colors Gradual Changing Table Lamp for Holiday Gifts or Home \\u2026",
      "url": "/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A02303021Y7K1FKL1N016&url=%2Fcrystal-Colors-Gradual-Changing-Holiday%2Fdp%2FB078BMJW27%2Fref%3Dsr_1_18_sspa%3Fdchild%3D1%26keywords%3Dpikachu%26sr%3D8-18-spons%26psc%3D1&qualifier=1604683213&id=1937612254046914&widgetName=sp_mtf",
      "rating": "4.2 out of 5 stars",
      "reviews": "118",
      "price": "$20.99"
    },
    {
      "title": "Funny Cartoon Head Face Mask Fashion Bandana Shield for Boy Girl Kids Outdoors Sports with Protective Filters",
      "url": "/gp/slredirect/picassoRedirect.html/ref=pa_sp_mtf_aps_sr_pg1_1?ie=UTF8&adId=A0957263F7GWFWGYEIC5&url=%2FFashion-Bandanas-Outdoors-Protective-Activated%2Fdp%2FB08H89H6XF%2Fref%3Dsr_1_19_sspa%3Fdchild%3D1%26keywords%3Dpikachu%26sr%3D8-19-spons%26psc%3D1&qualifier=1604683213&id=1937612254046914&widgetName=sp_mtf",
      "rating": "4.5 out of 5 stars",
      "reviews": "27",
      "price": "$15.66"
    },
    {
      "title": "Pok\\u00e9mon Petite Pals Hairband Plush, Pikachu",
      "url": "/Pok%C3%A9mon-Petite-Hairband-Plush-Pikachu/dp/B06W2H64Q5/ref=sr_1_43?dchild=1&keywords=pikachu&sr=8-43",
      "rating": "4.3 out of 5 stars",
      "reviews": "11",
      "price": "$11.99"
    },
    {
      "title": "NEWCOSPLAY Unisex Children Pikachu Onesies Halloween Cosplay Costume",
      "url": "/gp/slredirect/picassoRedirect.html/ref=pa_sp_btf_aps_sr_pg1_1?ie=UTF8&adId=A04196183JJ2H449JKGHQ&url=%2FNEWCOSPLAY-Cosplay-Onesies-Costume-Pikachu%2Fdp%2FB07BKVDFHH%2Fref%3Dsr_1_59_sspa%3Fdchild%3D1%26keywords%3Dpikachu%26sr%3D8-59-spons%26psc%3D1&qualifier=1604683213&id=1937612254046914&widgetName=sp_btf",
      "rating": "4.8 out of 5 stars",
      "reviews": "133",
      "price": "$30.99"
    },
    {
      "title": "NEWCOSPLAY Unisex Adult Pikachu Pyjamas Halloween Onesie Costume",
      "url": "/gp/slredirect/picassoRedirect.html/ref=pa_sp_btf_aps_sr_pg1_1?ie=UTF8&adId=A03029631U0H18XJPSCOO&url=%2FNEWCOSPLAY-Halloween-Pajamas-Cosplay-Costumes%2Fdp%2FB07GD95HDK%2Fref%3Dsr_1_60_sspa%3Fdchild%3D1%26keywords%3Dpikachu%26sr%3D8-60-spons%26psc%3D1&qualifier=1604683213&id=1937612254046914&widgetName=sp_btf",
      "rating": "4.6 out of 5 stars",
      "reviews": "173",
      "price": "$31.99"
    }
  ]
}
```
