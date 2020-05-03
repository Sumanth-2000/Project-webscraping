# Project-webscraping
webscraping of flipkart website

Step 1: Find the URL that you want to scrape
For this example, we are going scrape Flipkart website to extract the Price, Name, and Rating of Laptops. The URL for this page is https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2.

Step 2: Inspecting the Page
The data is usually nested in tags. So, we inspect the page to see, under which tag the data we want to scrape is nested. To inspect the page, just right click on the element and click on “Inspect”.

Step 3: Find the data you want to extract
Let’s extract the Price, Name, and Rating which is nested in the “div” tag respectively.

Step 4: Write the code
First, let’s create a Python file. To do this, open the terminal in Ubuntu and type gedit <your file name> with .py extension.

Step 6: Store the data in a required format
After extracting the data, you might want to store it in a format. This format varies depending on your requirement. For this example, we will store the extracted data in a CSV (Comma Separated Value) format. 
