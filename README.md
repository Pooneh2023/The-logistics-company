# 📦 Logistics Delivery Analysis

## 📊 Project Overview

This project analyzes the delivery process of a logistics company to identify operational delays, measure performance, and recommend improvements.

The analysis simulates the real-world logistics pipeline and evaluates how efficiently orders move from placement to delivery.

---

## 🎯 Business Objective

* Identify where delays occur in the delivery pipeline
* Measure processing time at each stage
* Detect variability and unreliable steps
* Provide actionable recommendations to reduce delivery time

---

## 🧱 Data Sources

* **Orders dataset** → order details, customer, timestamps
* **Campaign dataset** → arrival scan & campaign-related timing
* **Order Process dataset** → truck and processing timestamps
* **Internal Study dataset** → warehouse preparation & pickup

---

## ⚙️ Data Pipeline

1. Data Audit & Exploration
2. Data Cleaning (per dataset)
3. Data Merging into unified dataset
4. Delivery Logic Modeling (based on business rules)
5. KPI & Performance Analysis

---

## 🔄 Delivery Process Logic

The delivery process follows a rule-based system:

* Orders received on weekends are processed starting Monday
* Warehouse preparation takes ~2 days
* Trucks operate only on **Monday, Wednesday, Friday**
* Express orders bypass certain waiting steps

📌 See full flowchart: `assets/flowchart.png`

---

## 📈 Key Metrics (KPIs)

* **Total Delivery Time** (Order → Delivery)

* **Stage Processing Times**:

  * Order → Ready to Ship
  * Ready → Pickup
  * Pickup → Truck
  * Truck → Delivery

* **Variability (Standard Deviation)** per stage

* **Delay Distribution**

* **On-time Delivery Rate**

* **Outlier Detection** (extreme delays)

---

## 🔍 Key Insights

* The largest delay occurs between **Order Date → On Truck Scan Date**, indicating scheduling bottlenecks
* Limited truck days (Mon/Wed/Fri) create **queue accumulation and waiting time**
* High variability in processing times suggests **inconsistent operations**
* A small percentage of orders experience **extreme delays (outliers)**

---

## 💡 Recommendations

* Increase truck frequency (especially Tue/Thu)
* Optimize warehouse processing time
* Introduce better scheduling or batching strategy
* Monitor outliers to identify operational failures
* Consider prioritization for delayed orders

---

## 🛠 Tech Stack

* Python (pandas, numpy)
* Jupyter Notebooks
* Git & GitHub

---

## 📁 Project Structure

```bash
data/
 ├── raw/
 ├── cleaned/
 ├── final/

notebooks/
 ├── 01_data_audit.ipynb
 ├── ...
 ├── 06_merge_final_dataset.ipynb

src/
 └── data/

tests/
```

---

## 🚀 How to Run

```bash
uv run python main.py
```

---

## 📌 Future Improvements

* Add automated pipeline (Airflow / Prefect)
* Build dashboard (Power BI / Tableau)
* Add unit tests for data validation
* Deploy as API or reporting tool

```
```
