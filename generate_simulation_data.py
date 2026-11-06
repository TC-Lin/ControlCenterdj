# -*- coding: utf-8 -*-
import random
import json
import pandas as pd

random.seed(20261106)

BRANCH_CSV_RAW = """分行代號,分行名稱,業務分區,小分區,組別,分區
002,港都分行,南區,高雄,第一組,南區
003,楠梓分行,南區,高雄,第一組,南區
004,台中分行,中區,中區,第一組,中區
005,忠孝分行,北二區,北二區,第一組,其他北區
006,府城分行,南區,台南,第二組,南區
007,國外部,北一區,北一區,第一組,國外部
008,台北復興分行,北二區,北二區,第一組,其他北區
010,蘭雅分行,北一區,北一區,第一組,其他北區
012,三重分行,北一區,北一區,第二組,其他北區
013,新興分行,南區,高雄,第四組,南區
014,桃園分行,桃竹苗區,桃竹苗區,第二組,桃竹苗區
015,中山分行,北一區,北一區,第一組,其他北區
016,高雄加工出口區分行,南區,高雄,第二組,南區
017,城中分行,北二區,北二區,第二組,其他北區
018,北彰化分行,中區,中區,第一組,中區
019,安和分行,北二區,北二區,第二組,其他北區
020,竹科新安分行,桃竹苗區,桃竹苗區,第一組,桃竹苗區
021,天母分行,北一區,北一區,第二組,其他北區
022,嘉義分行,南區,台南,第二組,南區
023,花蓮分行,北二區,北二區,第五組,其他北區
026,北新竹分行,桃竹苗區,桃竹苗區,第二組,桃竹苗區
027,板南分行,北一區,北一區,第三組,其他北區
028,潭子分行,中區,中區,第二組,中區
029,桃園國際機場分行,桃竹苗區,桃竹苗區,第四組,桃竹苗區
030,南台北分行,北二區,北二區,第二組,其他北區
031,敦南分行,北二區,北二區,第四組,其他北區
032,員林分行,中區,中區,第一組,中區
034,永和分行,北二區,北二區,第三組,其他北區
035,豐原分行,中區,中區,第一組,中區
036,民生分行,北一區,北一區,第三組,其他北區
037,北台中分行,中區,中區,第一組,中區
038,三多分行,南區,高雄,第五組,南區
039,中壢分行,桃竹苗區,桃竹苗區,第三組,桃竹苗區
040,三民分行,南區,高雄,第四組,南區
041,新莊分行,北一區,北一區,第二組,其他北區
042,松南分行,北一區,北一區,第三組,其他北區
043,大同分行,北二區,北二區,第四組,其他北區
044,南台中分行,中區,中區,第一組,中區
045,鳳山分行,南區,高雄,第四組,南區
046,新店分行,北二區,北二區,第二組,其他北區
047,東高雄分行,南區,高雄,第四組,南區
048,信義分行,北一區,北一區,第四組,其他北區
049,基隆分行,北二區,北二區,第四組,其他北區
050,永康分行,南區,台南,第三組,南區
051,內湖分行,北二區,北二區,第一組,其他北區
052,岡山分行,南區,高雄,第三組,南區
053,屏東分行,南區,高雄,第五組,南區
055,松山機場分行,北一區,北一區,第三組,其他北區
056,土城分行,北一區,北一區,第四組,其他北區
057,大稻埕分行,北一區,北一區,第三組,其他北區
058,頭份分行,桃竹苗區,桃竹苗區,第四組,桃竹苗區
059,苓雅分行,南區,高雄,第五組,南區
060,沙鹿分行,中區,中區,第三組,中區
061,八德分行,桃竹苗區,桃竹苗區,第四組,桃竹苗區
062,宜蘭分行,北二區,北二區,第四組,其他北區
063,斗六分行,中區,中區,第四組,中區
064,南投分行,中區,中區,第三組,中區
065,東台南分行,南區,台南,第三組,南區
066,高雄國際機場分行,南區,高雄,第五組,南區
067,東內湖分行,北二區,北二區,第三組,其他北區
068,太平分行,中區,中區,第二組,中區
069,中和分行,北二區,北二區,第一組,其他北區
070,南京東路分行,北二區,北二區,第二組,其他北區
071,東台中分行,中區,中區,第三組,中區
072,北高雄分行,南區,高雄,第五組,南區
074,南港分行,北一區,北一區,第五組,其他北區
075,竹南科學園區分行,桃竹苗區,桃竹苗區,第五組,桃竹苗區
076,中科分行,中區,中區,第五組,中區
077,大甲分行,中區,中區,第四組,中區
079,金門分行,北一區,北一區,第五組,其他北區
080,南崁分行,桃竹苗區,桃竹苗區,第二組,桃竹苗區
083,向上分行,中區,中區,第五組,中區
103,仁武分行,南區,高雄,第五組,南區
201,金控總部分行,北一區,北一區,第一組,金控總部分行
202,台北分行,北二區,北二區,第一組,其他北區
203,新竹分行,桃竹苗區,桃竹苗區,第二組,桃竹苗區
204,中台中分行,中區,中區,第三組,中區
205,高雄分行,南區,高雄,第二組,南區
206,板橋分行,北一區,北一區,第四組,其他北區
207,桃興分行,桃竹苗區,桃竹苗區,第一組,桃竹苗區
208,竹北分行,桃竹苗區,桃竹苗區,第五組,桃竹苗區
210,敦化分行,北一區,北一區,第三組,其他北區
212,嘉興分行,南區,台南,第五組,南區
213,台南分行,南區,台南,第二組,南區
214,寶成分行,中區,中區,第二組,中區
215,竹科竹村分行,桃竹苗區,桃竹苗區,第一組,桃竹苗區
216,世貿分行,北二區,北二區,第三組,其他北區
219,南三重分行,北一區,北一區,第五組,其他北區
220,南彰化分行,中區,中區,第三組,中區
226,城東分行,北一區,北一區,第五組,其他北區
227,五福分行,南區,高雄,第五組,南區
228,羅東分行,北二區,北二區,第四組,其他北區
229,大安分行,北二區,北二區,第二組,其他北區
231,林口分行,桃竹苗區,桃竹苗區,第五組,桃竹苗區
232,后里分行,中區,中區,第三組,中區
233,鹿港分行,中區,中區,第四組,中區
234,圓山分行,北一區,北一區,第五組,其他北區
235,思源分行,北一區,北一區,第三組,其他北區
236,北中壢分行,桃竹苗區,桃竹苗區,第五組,桃竹苗區
237,內湖科學園區分行,北一區,北一區,第四組,其他北區
238,雙和分行,北二區,北二區,第四組,其他北區
240,衡陽分行,北一區,北一區,第四組,其他北區
241,大里分行,中區,中區,第三組,中區
242,台南科學園區分行,南區,台南,第五組,南區
078,成功簡易型分行,南區,高雄,第一組,南區
081,中鋼簡易型分行,南區,高雄,第一組,南區
116,高雄漁港簡易型分行,南區,高雄,第二組,南區
086,駐外交部簡易分行,北一區,北一區,第一組,國外部"""

# 解析分行主檔
branches = []
for line in BRANCH_CSV_RAW.strip().splitlines()[1:]:
    parts = [p.strip() for p in line.split(",")]
    branches.append({
        "code": parts[0],
        "name": parts[1],
        "region": parts[2],
        "subRegion": parts[3],
        "group": parts[4],
        "category": parts[5]
    })

df_branches = pd.DataFrame(branches)
df_branches.columns = ["分行代號", "分行名稱", "業務分區", "小分區", "組別", "分區"]
df_branches.to_csv("分行主檔.csv", index=False, encoding="utf-8-sig")
df_branches.to_excel("分行主檔.xlsx", index=False)

# 產生 2025-01 ~ 2026-11 共 23 個月份清單
months = []
for y in [2025, 2026]:
    max_m = 12 if y == 2025 else 11
    for m in range(1, max_m + 1):
        months.append(f"{y}-{m:02d}")

# 規模組別基準倍率 (第一組規模最大 ~ 第五組)
group_scale = {
    "第一組": 2.4,
    "第二組": 1.7,
    "第三組": 1.25,
    "第四組": 0.9,
    "第五組": 0.65
}

# 為全行 109 家分行生成 2025-01 ~ 2026-11 (23個月) 的月度統計序列 (支援任意月份 MoM 月增減、YoY 年增減)
# 結構紧凑：{ code, name, region, subRegion, group, category, custCount, gebCount, m: { "2025-01": [depWan, loanWan, limitWan, fundWan, fundNewWan, t1Contrib, visits, reports, closed, tracking, repWan, clsWan, weightTimes10, points, t2Contrib], ... } }
branch_monthly_data = []

for idx, b in enumerate(branches):
    scale = group_scale.get(b["group"], 1.0)
    if "簡易" in b["name"]:
        scale *= 0.45
    elif b["code"] in ["007", "201", "002", "004", "020", "005"]:
        scale *= 1.35

    cust_count = max(8, int(round(22 * scale + random.uniform(-3, 5))))
    geb_rate_base = min(0.95, max(0.45, 0.68 + random.uniform(-0.15, 0.20)))
    geb_count = int(round(cust_count * geb_rate_base))

    # 成長趨勢設定 (讓不同分行有成長、持平或微幅波動，反應真實 MoM / YoY 差異)
    annual_growth_dep = random.uniform(-0.06, 0.22)
    annual_growth_loan = random.uniform(-0.05, 0.25)
    annual_growth_fund = random.uniform(-0.08, 0.28)
    annual_growth_biz = random.uniform(-0.10, 0.32)

    base_dep = int(round(18000 * scale * random.uniform(0.85, 1.2)))    # 單位：萬
    base_loan = int(round(14000 * scale * random.uniform(0.85, 1.2)))   # 單位：萬
    base_limit = int(round(base_loan * random.uniform(1.35, 1.75)))     # 單位：萬
    base_fund = int(round(4200 * scale * random.uniform(0.8, 1.25)))    # 單位：萬

    m_dict = {}
    for m_idx, ym in enumerate(months):
        progress = m_idx / 12.0  # 12個月約等於1年
        season = 1.0 + 0.04 * ((m_idx % 4) - 1.5)
        noise_dep = random.uniform(0.96, 1.05)
        noise_loan = random.uniform(0.97, 1.04)
        noise_fund = random.uniform(0.94, 1.07)

        dep_w = max(500, int(round(base_dep * (1 + annual_growth_dep * progress) * season * noise_dep)))
        loan_w = max(300, int(round(base_loan * (1 + annual_growth_loan * progress) * season * noise_loan)))
        limit_w = max(loan_w + 500, int(round(base_limit * (1 + annual_growth_loan * 0.8 * progress))))
        fund_w = max(100, int(round(base_fund * (1 + annual_growth_fund * progress) * season * noise_fund)))
        fund_new_w = max(10, int(round(fund_w * random.uniform(0.06, 0.16))))
        t1_contrib = max(50, int(round((dep_w * 0.012 + loan_w * 0.018 + fund_w * 0.025))))

        # 表二：行員爭攬月度實績
        biz_factor = max(0.5, (1 + annual_growth_biz * progress) * random.uniform(0.85, 1.18))
        visits = max(3, int(round(10 * scale * biz_factor)))
        reports = max(2, min(visits, int(round(visits * random.uniform(0.68, 0.90)))))
        closed = max(1, min(reports, int(round(reports * random.uniform(0.45, 0.82)))))
        tracking = max(0, reports - closed)

        rep_w = max(500, int(round(reports * 1200 * scale * random.uniform(0.8, 1.3))))
        cls_w = max(200, int(round(rep_w * (closed / max(reports, 1)) * random.uniform(0.75, 1.15))))
        # 權重積分 = 0.2*visits + 0.3*reports + 0.5*closed
        weight_x10 = int(round((visits * 0.2 + reports * 0.3 + closed * 0.5) * 10))
        points = max(0, int(round(closed * random.uniform(0.15, 0.45))))
        t2_contrib = max(30, int(round(cls_w * 0.08 + points * 50 + weight_x10 * 8)))

        m_dict[ym] = [
            dep_w, loan_w, limit_w, fund_w, fund_new_w, t1_contrib,
            visits, reports, closed, tracking, rep_w, cls_w, weight_x10, points, t2_contrib
        ]

    branch_monthly_data.append({
        "code": b["code"],
        "name": b["name"],
        "region": b["region"],
        "subRegion": b["subRegion"],
        "group": b["group"],
        "category": b["category"],
        "custCount": cust_count,
        "gebCount": geb_count,
        "m": m_dict
    })

# 同時生成代表性客戶明細 (表一) 與行員爭攬明細 (表二)，確保每個業務分區與主要分行都有具體客戶與行員案件可鑽取與編輯
company_prefixes = [
    "大江生醫", "南科精密", "中台灣光電", "北極星航太", "永豐綠能", "亞太智慧物流",
    "台灣先進半導體", "長榮航太科技", "高港重工機械", "竹科晶圓材料", "華南精密模具", "府城生技製藥",
    "忠孝建設開發", "內科雲端數碼", "台中精機工業", "楠梓電子封裝", "桃園國際倉儲", "北彰五金製品",
    "敦南環球貿易", "竹北AI晶片", "板橋數位醫療", "員林食品工業", "岡山航太扣件", "大里精密光學"
]
industries = ["生技醫療業", "製造業", "科技業", "服務業", "傳統產業"]
clerk_names = [
    ("1234", "陳建宏", "營業"), ("1235", "林雅婷", "營業"), ("1236", "張志豪", "授信"),
    ("1237", "王建民", "理財"), ("1238", "黃詩涵", "營業"), ("1239", "劉冠宇", "授信"),
    ("1240", "蔡淑芬", "理財"), ("1241", "鄭家豪", "授信"), ("1242", "許瑋倫", "營業"),
    ("1243", "謝承恩", "授信"), ("1244", "吳欣怡", "理財"), ("1245", "周俊傑", "營業"),
    ("1246", "楊宗翰", "授信"), ("1247", "郭雅雯", "理財"), ("1248", "洪志明", "授信")
]

table1_rows = []
table2_rows = []

# 挑選前 30 家代表性分行 + 各區重點分行生成具體客戶與案件明細，其餘分行點擊時也會自動展示分行客戶與案件
featured_Indices = list(range(len(branches)))
cust_seq = 1
case_seq = 1

for b_idx, b in enumerate(branches):
    # 每家分行至少生成 1~2 戶代表客戶與 1~2 筆代表爭攬案件，重點分行生成更多
    n_cust = 2 if b_idx < 15 else 1
    for c_i in range(n_cust):
        cid = f"C{cust_seq:03d}"
        cname_short = f"客戶 {cust_seq}"
        comp_base = company_prefixes[(cust_seq - 1) % len(company_prefixes)]
        comp_full = f"{comp_base}（{b['name'][:2]}廠）股份有限公司" if cust_seq > len(company_prefixes) else f"{comp_base}股份有限公司"
        uni_no = f"{23000000 + cust_seq * 1873:08d}"
        ind = industries[cust_seq % len(industries)]
        rating = str(5 + (cust_seq % 3))
        tier = "A" if c_i == 0 else "B"
        ck_id, ck_name, ck_dept = clerk_names[(b_idx + c_i) % len(clerk_names)]

        dep_wan = random.choice([1500, 2000, 3200, 5000, 8000, 12000])
        fx_wan = random.choice([300, 500, 800, 1200, 2000])
        lim_wan = random.choice([3000, 5000, 8000, 15000, 30000, 100000])
        loan_wan = int(lim_wan * random.choice([0, 0.25, 0.4, 0.6]))
        fund_wan = random.choice([0, 500, 800, 1000, 1500, 3000])
        fund_m_wan = int(fund_wan * 0.2) if fund_wan > 0 else 0
        geb_st = random.choices(["已申辦", "申請中", "未申辦"], weights=[0.7, 0.15, 0.15])[0]
        pay_st = random.choices(["已申辦", "評估中", "未申辦"], weights=[0.65, 0.2, 0.15])[0]
        contrib_val = int(dep_wan * 0.04 + loan_wan * 0.05 + fund_wan * 0.06 + 80)

        def fmt_w(w):
            if w >= 10000 and w % 10000 == 0:
                return f"{w // 10000}億"
            return f"{w}萬" if w > 0 else "0"

        table1_rows.append({
            "資料日期": "2026-11",
            "客戶代號": cid,
            "客戶": cname_short,
            "統一編號": uni_no,
            "客戶全銜": comp_full,
            "產業別": ind,
            "信評": rating,
            "業務分區": b["region"],
            "小分區": b["subRegion"],
            "組別": b["group"],
            "分區": b["category"],
            "分行代號": b["code"],
            "分行名稱": b["name"],
            "分行歸屬": tier,
            "主責行員": ck_id,
            "存款餘額": fmt_w(dep_wan),
            "外幣存款餘額": fmt_w(fx_wan),
            "授信額度": fmt_w(lim_wan),
            "授信餘額": fmt_w(loan_wan),
            "基金餘額": fmt_w(fund_wan),
            "本月購買基金": fmt_w(fund_m_wan),
            "是否申辦網銀(GEB)": geb_st,
            "薪轉戶狀態": pay_st,
            "匯兌往來": random.choice(["經常往來", "有避險需求", "待評估"]),
            "進出口往來": random.choice(["經常往來", "有需求", "無"]),
            "貢獻": contrib_val,
            "公司電話": f"02-2345-{1000 + cust_seq:04d}",
            "公司地址": f"{b['subRegion']}工業區經貿路 {cust_seq} 號",
            "上次拜訪AI摘要": f"【{b['name']}】客戶營收穩健，評估下半年擴充產線與營運週轉金需求，持續推動授信與GEB網銀整合服務。"
        })

        # 生成對應的表二爭攬案件 (涵蓋 2026-11、2026-10、2025-11 等月份)
        case_ym = "2026-11" if c_i == 0 else random.choice(["2026-11", "2026-10", "2025-11"])
        biz_type = random.choice(["授信", "存款", "理財", "匯兌", "網銀GEB"])
        has_rep = "有"
        close_st = random.choices(["有", "追蹤"], weights=[0.68, 0.32])[0]
        rep_amt_w = random.choice([1500, 3000, 5000, 8000, 10000, 30000])
        cls_amt_w = int(rep_amt_w * random.choice([0.7, 1.0])) if close_st == "有" else 0
        weight_val = 1.0 if close_st == "有" else 0.5
        pts = 1 if (biz_type == "網銀GEB" or (close_st == "有" and cust_seq % 4 == 0)) else 0
        pts_note = "GEB申請" if pts > 0 else ""

        table2_rows.append({
            "案件編號": f"CASE-{case_ym.replace('-', '')}-{case_seq:03d}",
            "資料月份": case_ym,
            "日期": f"{int(case_ym[:4])-1911}{case_ym[5:7]}12",
            "行員": ck_id,
            "行員姓名": ck_name,
            "科別": ck_dept,
            "業務分區": b["region"],
            "小分區": b["subRegion"],
            "組別": b["group"],
            "分區": b["category"],
            "分行代號": b["code"],
            "分行名稱": b["name"],
            "訪客": random.choice(["約訪", "臨櫃", "電訪"]),
            "客戶代號": cid,
            "客戶": cname_short,
            "統一編號": uni_no,
            "分行歸屬": tier,
            "通報": has_rep,
            "通報業務": biz_type,
            "通報金額": fmt_w(rep_amt_w),
            "協作單位": "授信單位、營業單位" if biz_type == "授信" else "理財單位、營業單位",
            "成案": close_st,
            "推動進度說明": f"已核准撥款 {fmt_w(cls_amt_w)} 入帳" if close_st == "有" else f"{b['name']}財報徵提審查中，預計下週送區中心核決",
            "成案金額": fmt_w(cls_amt_w),
            "點數": pts,
            "點數說明": pts_note,
            "階段權重積分": weight_val,
            "案件貢獻": contrib_val,
            "營收狀況": random.choice(["成長", "成長", "持平"]),
            "預估成長幅度(%)": random.choice([10, 15, 20, 25]),
            "加班頻率": random.choice(["三班", "二班"]),
            "訪談重點紀錄": f"拜訪{comp_full}，確認產能滿載並洽談{biz_type}專案合作。",
            "風險與需求": f"提出{fmt_w(rep_amt_w)}{biz_type}需求與企業網銀(GEB)資金調度整合。",
            "後續行動": "追蹤核准額度動撥與GEB開通進度" if close_st == "有" else "補齊近三期401報表並協同審查部覆訪",
            "行動期限": "2026-11-28"
        })

        cust_seq += 1
        case_seq += 1

df_t1 = pd.DataFrame(table1_rows)
df_t1.to_csv("客戶每日狀態表.csv", index=False, encoding="utf-8-sig")
df_t1.to_excel("客戶每日狀態表.xlsx", index=False)

df_t2 = pd.DataFrame(table2_rows)
df_t2.to_csv("行員爭攬業務紀錄表.csv", index=False, encoding="utf-8-sig")
df_t2.to_excel("行員爭攬業務紀錄表.xlsx", index=False)

with open("sim_payload.json", "w", encoding="utf-8") as f:
    json.dump({
        "months": months,
        "branchMonthly": branch_monthly_data,
        "table1": table1_rows,
        "table2": table2_rows
    }, f, ensure_ascii=False)

print(f"Generated {len(branches)} branches across {len(months)} months, {len(table1_rows)} customers, {len(table2_rows)} solicitation records.")
