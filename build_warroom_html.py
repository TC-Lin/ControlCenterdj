# -*- coding: utf-8 -*-
import json

with open("sim_payload.json", "r", encoding="utf-8") as f:
    payload = json.load(f)

payload_json_str = json.dumps(payload, ensure_ascii=False)

HTML_TEMPLATE = """<!doctype html>
<html lang="zh-Hant">
<head>
  <meta name="ms-sp-authoring-source" content="agent">
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>銀行業務戰情室 (總處/區中心/分行權責 × 月增減/年增減版)</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    body {
      --nav: #082d5b;
      --blue: #2878e5;
      --bg: #eef4fa;
      --line: #d9e4ef;
      --text: #193653;
      --muted: #647b92;
      --green: #15803d;
      --amber: #d97706;
      --red: #c5353d;
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: "Microsoft JhengHei", system-ui, -apple-system, sans-serif;
    }
    * { box-sizing: border-box; }
    button, input, select, textarea { font: inherit; }
    button { cursor: pointer; }
    .app {
      min-height: 100vh;
      display: grid;
      grid-template-columns: 245px 1fr;
    }
    aside {
      background: linear-gradient(180deg, #082d5b, #051b38);
      color: #e8f2ff;
      padding: 15px;
      position: sticky;
      top: 0;
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow-y: auto;
    }
    .brand { font-weight: 900; font-size: 19px; letter-spacing: 0.5px; }
    .brand small { display: block; font-size: 12px; font-weight: 400; color: #9ec5ff; margin-top: 2px; }
    .nav { margin-top: 14px; }
    .nav a {
      display: flex;
      align-items: center;
      gap: 8px;
      color: #e4efff;
      text-decoration: none;
      padding: 10px 12px;
      border-radius: 9px;
      margin: 4px 0;
      font-weight: 700;
      font-size: 13px;
      transition: background 0.15s;
    }
    .nav a.active, .nav a:hover { background: #2672d6; }
    .rbac-panel {
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(158, 197, 255, 0.35);
      border-radius: 10px;
      padding: 11px;
      margin-top: 12px;
      font-size: 12px;
    }
    .rbac-panel b {
      color: #ffde7a;
      display: block;
      font-size: 13px;
      margin-bottom: 6px;
    }
    .rbac-panel label {
      display: block;
      font-size: 12px;
      color: #cfe3ff;
      margin: 6px 0 3px;
      font-weight: 700;
    }
    .rbac-panel select {
      width: 100%;
      padding: 6px 8px;
      border-radius: 6px;
      border: 1px solid #6b9be0;
      background: #0c356a;
      color: #fff;
      font-weight: 700;
      font-size: 12.5px;
    }
    .rbac-badge-box {
      margin-top: 8px;
      padding: 6px 8px;
      border-radius: 6px;
      background: rgba(22, 131, 74, 0.35);
      border: 1px solid #4ade80;
      color: #e2fbe8;
      font-size: 12px;
      line-height: 1.45;
    }
    .sidebar-box {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: 10px;
      padding: 9px;
      margin-top: 10px;
      font-size: 12px;
      line-height: 1.45;
    }
    .sidebar-box b { color: #fff; display: block; margin-bottom: 3px; }
    .sidebar-box .file-btn {
      display: block;
      width: 100%;
      text-align: center;
      background: rgba(40, 120, 229, 0.35);
      border: 1px solid #5a9cf5;
      color: #fff;
      padding: 5px 8px;
      border-radius: 6px;
      margin-top: 5px;
      font-size: 12px;
      cursor: pointer;
    }
    .sidebar-box .file-btn:hover { background: #2878e5; }
    .note {
      font-size: 12px;
      border: 1px solid #49617e;
      padding: 8px;
      border-radius: 8px;
      color: #bdd3ec;
      margin-top: 10px;
    }
    .main { padding: 14px 18px; max-width: 1650px; }
    .top {
      background: linear-gradient(90deg, #113d73, #1680d5, #0c2d5a);
      color: white;
      padding: 12px 18px;
      border-radius: 13px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }
    .top small { display: block; font-size: 12px; font-weight: 400; opacity: 0.92; margin-top: 2px; }
    .ticker {
      background: #fff9db;
      border: 1px solid #f5d47a;
      border-left: 5px solid #f59f00;
      border-radius: 10px;
      padding: 7px 12px;
      margin: 10px 0;
      display: flex;
      align-items: center;
      gap: 10px;
      color: #664400;
      font-size: 13px;
    }
    .ticker-viewport {
      flex: 1;
      overflow: hidden;
      white-space: nowrap;
    }
    .ticker-track {
      display: inline-block;
      animation: scroll 105s linear infinite;
    }
    .ticker-viewport:hover .ticker-track,
    .ticker-track.paused {
      animation-play-state: paused;
    }
    .ticker-controls {
      display: flex;
      align-items: center;
      gap: 5px;
      flex-shrink: 0;
      background: rgba(255,255,255,0.8);
      padding: 3px 7px;
      border-radius: 7px;
      border: 1px solid #ecd078;
      font-size: 12px;
    }
    .ticker-controls select, .ticker-controls button {
      font-size: 12px;
      padding: 2px 6px;
      border-radius: 5px;
      border: 1px solid #d8bc66;
      background: #fff;
      color: #5c3d00;
      font-weight: 700;
    }
    @keyframes scroll {
      from { transform: translateX(12%); }
      to { transform: translateX(-100%); }
    }
    .page { display: none; }
    .page.active { display: block; }
    .grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }
    .card {
      background: white;
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 15px;
      margin-bottom: 12px;
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.02);
    }
    .title {
      font-weight: 900;
      font-size: 16px;
      margin-bottom: 11px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      flex-wrap: wrap;
    }
    .demo {
      display: inline-block;
      background: #e7f1ff;
      color: #0d509c;
      border-radius: 99px;
      padding: 3px 9px;
      font-size: 12px;
      font-weight: 700;
    }
    .demo.amber { background: #fff1cf; color: #795000; }
    .demo.green { background: #dcfce7; color: #166534; }
    .demo.red { background: #fee2e2; color: #991b1b; }
    .sub { font-size: 12px; color: var(--muted); line-height: 1.6; }
    .fields {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 9px;
    }
    .fields-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 9px;
    }
    .field label {
      display: block;
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 4px;
      color: #50677d;
    }
    .field input, .field select, .field textarea {
      width: 100%;
      padding: 7px 10px;
      border: 1px solid #cbd8e5;
      border-radius: 7px;
      color: var(--text);
      background: #fbfdff;
      font-size: 13px;
    }
    textarea { min-height: 68px; }
    .btn {
      border: 1px solid #c5d4e4;
      background: #fff;
      color: #244666;
      border-radius: 8px;
      padding: 7px 12px;
      font-weight: 700;
      font-size: 13px;
      transition: all 0.15s;
    }
    .btn:hover { background: #f0f6fc; }
    .btn.primary {
      background: var(--blue);
      border-color: var(--blue);
      color: white;
    }
    .btn.primary:hover { background: #1c64c9; }
    .btn.success {
      background: var(--green);
      border-color: var(--green);
      color: white;
    }
    .row {
      display: flex;
      gap: 8px;
      align-items: center;
      flex-wrap: wrap;
    }
    .metric {
      padding: 11px 13px;
      background: #f5f9fe;
      border: 1px solid #dce8f5;
      border-radius: 10px;
      margin: 2px 0;
    }
    .metric span.m-lbl { font-size: 12px; color: var(--muted); display: block; font-weight: 700; }
    .metric b.m-val { font-size: 18px; color: var(--nav); display: block; margin: 3px 0; }
    .delta-row {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      font-size: 12px;
      font-weight: 700;
      margin-top: 3px;
    }
    .delta-up { color: #15803d; background: #dcfce7; padding: 1px 6px; border-radius: 4px; }
    .delta-down { color: #b91c1c; background: #fee2e2; padding: 1px 6px; border-radius: 4px; }
    .delta-flat { color: #475569; background: #e2e8f0; padding: 1px 6px; border-radius: 4px; }
    .products {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
    }
    .product {
      background: #f5f9fc;
      border: 1px solid #e3edf7;
      padding: 10px;
      border-radius: 8px;
      font-size: 13px;
    }
    .product b { display: block; color: #47627d; font-size: 12px; margin-bottom: 3px; }
    .product .val { font-size: 15px; font-weight: 800; color: var(--nav); }
    .summary {
      background: #f5f8fb;
      border: 1px solid #e1eaf2;
      padding: 11px;
      border-radius: 8px;
      white-space: pre-wrap;
      line-height: 1.65;
      font-size: 13px;
    }
    .status {
      background: #fff8e9;
      border-left: 4px solid #d6a33e;
      padding: 10px 12px;
      border-radius: 7px;
      font-size: 13px;
      line-height: 1.6;
      margin-bottom: 8px;
    }
    .check label {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 10px;
      background: #f7fafc;
      border: 1px solid #e3ebf2;
      border-radius: 7px;
      margin: 4px 4px 4px 0;
      font-size: 13px;
      cursor: pointer;
    }
    .check.block label { display: flex; margin: 5px 0; }
    .check input { width: auto; }
    .report {
      white-space: pre-wrap;
      background: #fbfdff;
      border: 1px solid var(--line);
      padding: 15px;
      border-radius: 8px;
      line-height: 1.75;
      font-size: 14px;
    }
    .score { font-size: 22px; font-weight: 900; }
    .chartgrid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }
    .chartbox { height: 245px; position: relative; }
    .chart-zoom-btn {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      background: #082d5b;
      color: #fff;
      border: 1px solid #082d5b;
      border-radius: 6px;
      padding: 4px 10px;
      font-size: 12px;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(8, 45, 91, 0.18);
      transition: all 0.15s;
      white-space: nowrap;
    }
    .chart-zoom-btn:hover {
      background: #2878e5;
      border-color: #2878e5;
      transform: translateY(-1px);
    }
    .chart-zoom-float {
      position: absolute;
      right: 6px;
      bottom: 4px;
      z-index: 5;
      opacity: 0.86;
      padding: 3px 8px;
      font-size: 11.5px;
      background: rgba(8, 45, 91, 0.88);
    }
    .chart-zoom-float:hover {
      opacity: 1;
    }
    .zoom-modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(8, 28, 56, 0.68);
      backdrop-filter: blur(3px);
      z-index: 9500;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }
    .zoom-modal-card {
      background: #fff;
      border: 2px solid #9ec5ff;
      border-radius: 14px;
      width: min(92vw, 1260px);
      max-height: 90vh;
      margin: auto;
      display: flex;
      flex-direction: column;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35);
      overflow: hidden;
    }
    .zoom-modal-header {
      background: linear-gradient(90deg, #082d5b, #144987);
      color: #fff;
      padding: 12px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .zoom-modal-body {
      padding: 16px 20px;
      overflow: auto;
      background: #fbfdff;
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .zoom-chart-stage {
      background: #fff;
      border: 1px solid #d9e4ef;
      border-radius: 10px;
      padding: 14px 18px;
      width: 100%;
      min-height: 410px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin: auto;
    }
    .zoom-chart-stage svg {
      height: 390px !important;
      width: 100% !important;
      display: block;
      margin: 0 auto;
    }
    .zoom-modal-footer {
      padding: 12px 20px;
      background: #eef5fc;
      border-top: 1px solid #cde0f5;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }
    .full { grid-column: 1 / -1; }
    .toast {
      position: fixed;
      right: 18px;
      top: 75px;
      background: #082d5b;
      color: white;
      padding: 10px 16px;
      border-radius: 8px;
      display: none;
      z-index: 9999;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
      font-weight: 700;
      font-size: 13px;
    }
    .table-wrap {
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 8px;
      max-height: 440px;
    }
    table.data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12.5px;
      text-align: left;
    }
    table.data-table th {
      background: #f0f5fa;
      color: var(--nav);
      padding: 9px 10px;
      position: sticky;
      top: 0;
      border-bottom: 2px solid #cbd8e5;
      white-space: nowrap;
      z-index: 2;
    }
    table.data-table td {
      padding: 8px 10px;
      border-bottom: 1px solid #e8eff6;
      white-space: nowrap;
    }
    table.data-table tr:hover {
      background: #f4f9ff;
      cursor: pointer;
    }
    table.data-table tr.selected-row {
      background: #e1effe;
      font-weight: 700;
    }
    .sub-tabs {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      margin: 12px 0;
      border-bottom: 2px solid #dde7f2;
      padding-bottom: 8px;
    }
    .sub-tab {
      border: 1px solid #c9d8e8;
      background: #f5f9fd;
      color: #2c4c6e;
      padding: 7px 13px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.15s;
    }
    .sub-tab:hover { background: #e3effc; }
    .sub-tab.active {
      background: var(--nav);
      border-color: var(--nav);
      color: #fff;
    }
    .war-panel { display: none; }
    .war-panel.active { display: block; }
    .heat-bar {
      height: 6px;
      border-radius: 99px;
      background: #e2e8f0;
      margin-top: 3px;
      overflow: hidden;
      width: 85px;
    }
    .heat-fill {
      height: 100%;
      border-radius: 99px;
      background: linear-gradient(90deg, #3b82f6, #1d4ed8);
    }
    .selector-bar {
      background: #fff;
      border: 1px solid var(--line);
      border-radius: 11px;
      padding: 9px 14px;
      margin-top: 10px;
      display: flex;
      gap: 12px;
      align-items: center;
      flex-wrap: wrap;
    }
    .selector-group {
      display: flex;
      align-items: center;
      gap: 8px;
      flex: 1;
      min-width: 230px;
    }
    .selector-group label {
      font-size: 12px;
      font-weight: 800;
      color: var(--nav);
      white-space: nowrap;
      background: #e8f1fb;
      padding: 5px 9px;
      border-radius: 6px;
    }
    .selector-group select {
      flex: 1;
      padding: 6px 10px;
      border: 1px solid #b8cce0;
      border-radius: 7px;
      font-weight: 700;
      font-size: 13px;
      color: var(--text);
      background: #fbfdff;
    }
    .weight-pill {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      background: #f0f7ff;
      border: 1px solid #b9d6fb;
      padding: 8px 12px;
      border-radius: 9px;
      font-size: 13px;
      margin: 8px 0;
    }
    .weight-step {
      padding: 3px 8px;
      border-radius: 6px;
      background: #e2e8f0;
      color: #475569;
      font-weight: 700;
      font-size: 12px;
    }
    .weight-step.on { background: #2878e5; color: #fff; }
    .control-strip {
      background: #f4f8fd;
      border: 1px solid #cfe0f2;
      border-radius: 10px;
      padding: 10px 14px;
      margin-bottom: 12px;
      display: flex;
      gap: 12px;
      align-items: center;
      flex-wrap: wrap;
    }
    .control-strip label {
      font-size: 12px;
      font-weight: 800;
      color: var(--nav);
    }
    .control-strip select, .control-strip input {
      padding: 5px 9px;
      border-radius: 6px;
      border: 1px solid #b6cbe2;
      font-size: 13px;
      font-weight: 700;
      background: #fff;
      color: var(--text);
    }
    .slider-bar-wrap {
      margin-top: 8px;
      background: #f0f6fd;
      border: 1px solid #cce0f5;
      border-radius: 9px;
      padding: 7px 11px;
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }
    .slider-bar-wrap input[type="range"] {
      flex: 1;
      min-width: 140px;
      accent-color: #2878e5;
      cursor: pointer;
      height: 6px;
    }
    .slider-btn {
      border: 1px solid #b8cfe8;
      background: #fff;
      color: #193653;
      border-radius: 6px;
      padding: 3px 8px;
      font-size: 12px;
      font-weight: 800;
      cursor: pointer;
    }
    .slider-btn:hover { background: #e2effd; }
    .metric-pill-group {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .metric-pill {
      border: 1px solid #c5d6e8;
      background: #fff;
      color: #284b6e;
      padding: 5px 11px;
      border-radius: 99px;
      font-size: 12.5px;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.15s;
    }
    .metric-pill:hover { background: #eaf3fc; }
    .metric-pill.active {
      background: #2878e5;
      border-color: #2878e5;
      color: #fff;
      box-shadow: 0 2px 6px rgba(40, 120, 229, 0.28);
    }
    .branch-chip-list {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      max-height: 115px;
      overflow-y: auto;
      padding: 6px;
      background: #fff;
      border: 1px solid #d5e3f0;
      border-radius: 8px;
      margin-top: 6px;
    }
    .branch-chip {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 9px;
      border-radius: 99px;
      border: 1px solid #cbd8e6;
      background: #f8fbff;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      user-select: none;
    }
    .branch-chip.on {
      background: #e1effe;
      border-color: #2878e5;
      color: #082d5b;
    }
    .region-sum-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-top: 6px;
      margin-bottom: 12px;
    }
    .region-sum-card {
      background: linear-gradient(180deg, #ffffff, #f5f9ff);
      border: 1.5px solid #cde0f5;
      border-radius: 10px;
      padding: 10px 11px;
      cursor: pointer;
      transition: all 0.15s;
      position: relative;
    }
    .region-sum-card:hover {
      border-color: #2878e5;
      box-shadow: 0 3px 10px rgba(40, 120, 229, 0.14);
      transform: translateY(-1px);
    }
    .region-sum-card.active {
      background: linear-gradient(180deg, #eaf3ff, #dbeafe);
      border-color: #1d4ed8;
      box-shadow: 0 3px 10px rgba(29, 78, 216, 0.2);
    }
    .region-sum-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-weight: 900;
      font-size: 13.5px;
      color: var(--nav);
      margin-bottom: 6px;
      padding-bottom: 4px;
      border-bottom: 1px dashed #cbd8e6;
    }
    .region-sum-row {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      font-size: 12px;
      margin: 3px 0;
    }
    .region-sum-row b {
      color: #082d5b;
      font-size: 13px;
    }
    @media(max-width: 1180px) {
      .region-sum-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media(max-width: 960px) {
      .app { grid-template-columns: 1fr; }
      aside { height: auto; position: static; }
      .grid, .chartgrid, .fields-4 { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <div class="toast" id="toast"></div>
  <div class="app">
    <aside>
      <div>
        <div class="brand">🏦 銀行業務戰情室<small>總處 ＞ 各區中心 ＞ 分行權責平台</small></div>

        <!-- 權責身分切換器 (RBAC) -->
        <div class="rbac-panel">
          <b>🔐 單位權責檢核身分 (RBAC)</b>
          <label>1. 選擇檢核層級：</label>
          <select id="rbacRole">
            <option value="HQ">🏛️ 總處 (檢視全體/各區/108分行)</option>
            <option value="REGION">🗺️ 各區中心 (檢視轄區各分行/分行內)</option>
            <option value="BRANCH">🏢 分行長官 (檢視單一分行內部狀況)</option>
          </select>

          <div id="rbacRegionBox" style="display:none">
            <label>2. 選擇管轄業務分區：</label>
            <select id="rbacRegionSelect">
              <option value="北區">北區營運中心（原北一＋北二）</option>
              <option value="桃竹苗區">桃竹苗區營運中心</option>
              <option value="中區">中區營運中心</option>
              <option value="南區">南區營運中心</option>
            </select>
          </div>

          <div id="rbacBranchBox" style="display:none">
            <label>2. 選擇管轄分行 (108家)：</label>
            <select id="rbacBranchSelect"></select>
          </div>

          <div class="rbac-badge-box" id="rbacStatusText">
            目前權責：【總處】可檢視全行 4 大業務分區（北區／桃竹苗區／中區／南區）、108 家分行及各分行內部狀況。
          </div>
        </div>

        <nav class="nav">
          <a class="active" href="#warroom" data-page="warroom">📊 <span>權責戰情室 (月增減/年增減)</span></a>
          <a href="#customer" data-page="customer">🏠 <span>客戶概況 (表一+表二)</span></a>
          <a href="#interview" data-page="interview">📋 <span>業務爭攬與推動 (表二)</span></a>
          <a href="#marketing" data-page="marketing">📄 <span>行銷拜訪報告</span></a>
        </nav>

        <div class="sidebar-box">
          <b>📂 雙資料表與108分行主檔</b>
          <div id="t1Status">已載入 108 家分行 × 23 個月(2025/01~2026/11) 模擬資料</div>
          <label class="file-btn">
            ⬆️ 匯入客戶每日狀態 (.csv)
            <input type="file" id="uploadT1" accept=".csv" style="display:none">
          </label>
          <label class="file-btn">
            ⬆️ 匯入行員爭攬紀錄 (.csv)
            <input type="file" id="uploadT2" accept=".csv" style="display:none">
          </label>
          <button class="file-btn" id="exportT2Btn" style="margin-top:5px;background:rgba(22,131,74,0.45);border-color:#4ade80">
            ⬇️ 匯出最新爭攬紀錄 (.csv)
          </button>
        </div>
      </div>

      <div class="note">
        <b>權責與增減率邏輯</b><br>
        • <b>權責</b>：總處 ➔ 各區中心 ➔ 分行長官<br>
        • <b>MoM 月增減</b>：對照上月同期<br>
        • <b>YoY 年增減</b>：對照去年同月<br>
        • <b>模擬區間</b>：2025/01 ～ 2026/11
      </div>
    </aside>

    <main class="main">
      <header class="top">
        <div>
          <b id="topHeaderTitle">🏦 全行業務與績效戰情室 — 【總處視角】全體・各區・108家分行檢核看板</b>
          <small>資料範圍：2025年01月 ～ 2026年11月（支援月增減 MoM、年增減 YoY、雙資料表連動下鑽）</small>
        </div>
        <span id="clock" style="font-weight:700;font-size:13px"></span>
      </header>

      <!-- 重大案件跑馬燈 (含慢速與門檻控制) -->
      <div class="ticker">
        <div class="ticker-viewport">
          <span class="ticker-track" id="tickerMessage">📢 載入轄下重大追蹤案件動態中...</span>
        </div>
        <div class="ticker-controls no-print">
          <label>播報：</label>
          <select id="tickerFilter">
            <option value="PENDING">🔥 轄下未結追蹤案</option>
            <option value="MAJOR">💎 重大案件 (≥3,000萬)</option>
            <option value="ALL">📢 轄下全部動態</option>
          </select>
          <label>速度：</label>
          <select id="tickerSpeed">
            <option value="135s">🐢 慢速</option>
            <option value="100s" selected>🚶 適中</option>
            <option value="60s">⚡ 較快</option>
          </select>
          <button type="button" id="tickerPauseBtn">⏸️ 暫停</button>
        </div>
      </div>

      <!-- ==================== PAGE 1 (DEFAULT): 權責戰情室 (總處 > 各區 > 分行 × MoM/YoY) ==================== -->
      <section class="page active" id="page-warroom">
        <div class="card">
          <!-- 檢核基準月份與多維度過濾列 -->
          <div class="control-strip">
            <div>
              <label>📅 檢核基準月份：</label>
              <select id="warMonthSelect"></select>
            </div>
            <div id="warComparisonInfo" class="sub" style="font-weight:700;color:#0d509c;background:#e6f0fd;padding:4px 10px;border-radius:6px">
              月增減 (MoM) 對照：2026-10 ｜ 年增減 (YoY) 對照：2025-11
            </div>
            <div id="filterRegionWrap">
              <label>業務分區篩選：</label>
              <select id="warRegionFilter">
                <option value="ALL">全行 4 大業務分區</option>
                <option value="北區">北區（原北一＋北二）</option>
                <option value="桃竹苗區">桃竹苗區</option>
                <option value="中區">中區</option>
                <option value="南區">南區</option>
              </select>
            </div>
            <div id="filterGroupWrap">
              <label>組別篩選：</label>
              <select id="warGroupFilter">
                <option value="ALL">全部組別 (一~五組)</option>
                <option value="第一組">第一組</option>
                <option value="第二組">第二組</option>
                <option value="第三組">第三組</option>
                <option value="第四組">第四組</option>
                <option value="第五組">第五組</option>
              </select>
            </div>
            <div id="filterSearchWrap">
              <label>🔎 搜尋分行：</label>
              <input id="warBranchSearch" type="text" placeholder="輸入代號或名稱 (如 002, 港都)..." style="width:185px">
            </div>
          </div>

          <!-- 表一 KPI (含 MoM 月增減 & YoY 年增減) -->
          <div class="sub" style="font-weight:800;color:var(--nav);margin-bottom:4px">
            🏦 【表一：轄下客戶每日狀態基盤彙總】— 當月實績 × 月增減 (MoM) × 年增減 (YoY)
          </div>
          <div class="fields-4" style="margin-bottom:12px">
            <div class="metric">
              <span class="m-lbl">💰 轄下總存款餘額 (台+外幣)</span>
              <b class="m-val" id="kpiT1Deposit">NT$ 0</b>
              <div class="delta-row" id="deltaT1Deposit"></div>
            </div>
            <div class="metric">
              <span class="m-lbl">🤝 轄下總授信餘額 (額度動用率)</span>
              <b class="m-val" id="kpiT1Loan">NT$ 0</b>
              <div class="delta-row" id="deltaT1Loan"></div>
            </div>
            <div class="metric">
              <span class="m-lbl">📈 轄下總基金餘額 (本月新購)</span>
              <b class="m-val" id="kpiT1Fund">NT$ 0</b>
              <div class="delta-row" id="deltaT1Fund"></div>
            </div>
            <div class="metric">
              <span class="m-lbl">🌐 網銀 GEB 申辦率 & 基盤貢獻度</span>
              <b class="m-val" id="kpiT1Geb">0%</b>
              <div class="delta-row" id="deltaT1Contrib"></div>
            </div>
          </div>

          <!-- 表二 KPI (含 MoM 月增減 & YoY 年增減) -->
          <div class="sub" style="font-weight:800;color:var(--nav);margin-bottom:4px">
            🚀 【表二：轄下行員爭攬業務與後續推動彙總】— 當月實績 × 月增減 (MoM) × 年增減 (YoY)
          </div>
          <div class="fields-4">
            <div class="metric">
              <span class="m-lbl">📋 當月爭攬拜訪件數 (報/成/追)</span>
              <b class="m-val" id="kpiT2Cases">0 件</b>
              <div class="delta-row" id="deltaT2Cases"></div>
            </div>
            <div class="metric">
              <span class="m-lbl">📢 當月通報商機總金額</span>
              <b class="m-val" id="kpiT2ReportAmt">NT$ 0</b>
              <div class="delta-row" id="deltaT2ReportAmt"></div>
            </div>
            <div class="metric">
              <span class="m-lbl">✅ 當月實際成案總金額</span>
              <b class="m-val" id="kpiT2CloseAmt" style="color:var(--green)">NT$ 0</b>
              <div class="delta-row" id="deltaT2CloseAmt"></div>
            </div>
            <div class="metric">
              <span class="m-lbl">🏆 當月階段權重積分 & 爭攬貢獻</span>
              <b class="m-val" id="kpiT2Score">0.0 分</b>
              <div class="delta-row" id="deltaT2Score"></div>
            </div>
          </div>

          <!-- ==================== 總處專屬：直接檢視「全行 4 大業務分區（北區／桃竹苗區／中區／南區）總和與各區發展狀況圖表」專區 ==================== -->
          <div id="hqRegionTotalsSection" style="margin-top:12px">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px">
              <div class="sub" style="font-weight:900;color:var(--nav);font-size:13px">
                🗺️ 【總處各區總和與發展狀況直覽】全行 4 大業務分區（北區［原北一＋北二合併］／桃竹苗區／中區／南區）表一＆表二總和與增減率
                <span style="font-weight:400;color:#647b92">（點擊任一區卡片可快速篩選該區轄下分行）</span>
              </div>
              <div style="display:flex;gap:6px;flex-wrap:wrap">
                <button type="button" class="slider-btn" id="btnToggleHqRegCharts" style="background:#082d5b;border-color:#082d5b;color:#fff">
                  📊 收合／展開「4 大分區發展狀況圖表」
                </button>
                <button type="button" class="slider-btn" id="btnQuickCompareRegions" style="background:#e8f1fb;border-color:#2878e5;color:#082d5b">
                  🔗 同步帶入下方比較表
                </button>
                <button type="button" class="slider-btn" id="btnResetAllRegions" style="display:none;background:#fee2e2;border-color:#ef4444;color:#991b1b">
                  🔄 恢復檢視全行 4 大分區
                </button>
              </div>
            </div>
            <div class="region-sum-grid" id="hqRegionTotalsGrid"></div>

            <!-- 總處專屬：如同檢視各分行圖表的方式，直接檢視「全行 4 大業務分區（北區／桃竹苗區／中區／南區）」發展狀況圖表 -->
            <div id="hqRegionsChartsPanel" class="card" style="margin-bottom:12px;border:1.5px solid #93c5fd;background:#f4f9ff;padding:12px">
              <div class="title" style="margin-bottom:8px">
                <span>🏛️ 【總處檢視各區發展狀況】全行 4 大業務分區（北區／桃竹苗區／中區／南區）表一＆表二實績對比與逐月增減趨勢圖</span>
                <span class="demo">直接對比 4 大分區發展狀況（支援左上角切換業務、右側單位座標、6個月拉 BAR 與右下角放大檢視）</span>
              </div>

              <!-- 第一排：4 大業務分區之表一（存款/授信/基金）與表二（通報/成案）柱狀圖 -->
              <div class="chartgrid" style="margin-bottom:10px">
                <div class="card" style="margin-bottom:0;padding:11px;background:#fff">
                  <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:4px">
                    <b id="hqRegT1Title" style="font-size:13px;color:var(--nav)">🏦 表一：全行 4 大業務分區「存款／授信／基金總和」對比（單位：百萬）</b>
                    <button type="button" class="chart-zoom-btn" data-zoom-chart="chartHqRegT1" title="放大檢視此圖表">🔍 放大檢視</button>
                  </div>
                  <div class="chartbox" id="chartHqRegT1" style="height:225px"></div>
                </div>
                <div class="card" style="margin-bottom:0;padding:11px;background:#fff">
                  <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:4px">
                    <b id="hqRegT2Title" style="font-size:13px;color:var(--nav)">🚀 表二：全行 4 大業務分區「通報商機 vs 實際成案總和」對比（單位：百萬）</b>
                    <button type="button" class="chart-zoom-btn" data-zoom-chart="chartHqRegT2" title="放大檢視此圖表">🔍 放大檢視</button>
                  </div>
                  <div class="chartbox" id="chartHqRegT2" style="height:225px"></div>
                </div>
              </div>

              <!-- 第二排：4 大業務分區之【三期餘額對比柱狀圖】×【6個月逐月 MoM/YoY 成長率折線 ＋ 各月餘額柱狀圖】 -->
              <div class="chartgrid">
                <div class="card" style="margin-bottom:0;padding:11px;background:#fff">
                  <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:4px">
                    <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
                      <span style="font-size:13.5px;font-weight:900;color:var(--nav)">📊 4 大分區</span>
                      <select id="hqRegBarMetricSelect" style="width:auto;padding:3px 8px;font-size:13px;font-weight:900;color:#082d5b;border:1.5px solid #2878e5;border-radius:6px;background:#eef5fc;cursor:pointer">
                        <option value="dep">【總存款餘額 (表一)】</option>
                        <option value="loan">【總授信餘額 (表一)】</option>
                        <option value="fund">【基金餘額 (表一)】</option>
                        <option value="rep">【通報商機金額 (表二)】</option>
                        <option value="cls">【實際成案金額 (表二)】</option>
                        <option value="weight">【階段權重積分 (表二)】</option>
                        <option value="contrib">【綜合總貢獻 (雙表)】</option>
                      </select>
                      <b id="hqRegBarTitle" style="font-size:12.5px;color:var(--nav)">三期餘額柱狀圖（去年同月／上月／當月）</b>
                    </div>
                    <button type="button" class="chart-zoom-btn" data-zoom-chart="chartHqRegBar" title="放大檢視此圖表">🔍 放大檢視</button>
                  </div>
                  <div class="chartbox" id="chartHqRegBar" style="height:245px"></div>
                </div>

                <div class="card" style="margin-bottom:0;padding:11px;background:#fff">
                  <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:4px">
                    <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
                      <span style="font-size:13.5px;font-weight:900;color:var(--nav)">📈 4 大分區</span>
                      <select id="hqRegLineMetricSelect" style="width:auto;padding:3px 8px;font-size:13px;font-weight:900;color:#082d5b;border:1.5px solid #2878e5;border-radius:6px;background:#eef5fc;cursor:pointer">
                        <option value="dep">【總存款餘額 (表一)】</option>
                        <option value="loan">【總授信餘額 (表一)】</option>
                        <option value="fund">【基金餘額 (表一)】</option>
                        <option value="rep">【通報商機金額 (表二)】</option>
                        <option value="cls">【實際成案金額 (表二)】</option>
                        <option value="weight">【階段權重積分 (表二)】</option>
                        <option value="contrib">【綜合總貢獻 (雙表)】</option>
                      </select>
                      <select id="hqRegModeSelect" style="width:auto;padding:3px 8px;font-size:12.5px;font-weight:800;color:#082d5b;border:1.5px solid #2878e5;border-radius:6px;background:#fff;cursor:pointer">
                        <option value="MOM">逐月月增減率 MoM (%) 折線＋餘額柱</option>
                        <option value="YOY">逐月年增減率 YoY (%) 折線＋餘額柱</option>
                        <option value="RAW">逐月實際數值趨勢折線＋餘額柱</option>
                      </select>
                    </div>
                    <span class="demo" id="hqRegLineUnitBadge">窗格維持 6 個月</span>
                  </div>
                  <div class="chartbox" id="chartHqRegLine" style="height:245px"></div>
                  <!-- 4 大分區專屬：月份拉 BAR（維持 6 個月） -->
                  <div class="slider-bar-wrap" style="margin-top:8px;background:#eef5fc;border-color:#9ec5ff">
                    <button type="button" class="slider-btn" id="btnHqRegMonPrev6" title="往前 6 個月">⏮ -6月</button>
                    <button type="button" class="slider-btn" id="btnHqRegMonPrev1" title="往前 1 個月">◀</button>
                    <span style="font-size:12px;font-weight:800;color:var(--nav)">📅 各區發展月份拉 BAR（維持 6 個月）：</span>
                    <input type="range" id="sliderHqRegMonths" min="0" max="16" step="1" value="16">
                    <button type="button" class="slider-btn" id="btnHqRegMonNext1" title="往後 1 個月">▶</button>
                    <button type="button" class="slider-btn" id="btnHqRegMonNext6" title="往後 6 個月">+6月 ⏭</button>
                    <span class="demo amber" id="hqRegMonthRangeText" style="font-size:11px">2026-06 ～ 2026-11</span>
                    <button type="button" class="chart-zoom-btn" data-zoom-chart="chartHqRegLine" style="margin-left:auto" title="放大檢視此圖表">🔍 放大檢視</button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 戰情室多角度切換頁籤 (依權責動態調整顯示) -->
          <div class="sub-tabs" id="warSubTabs">
            <button type="button" class="sub-tab active" data-wtab="branch-overview" id="tabBtnBranch">🏦 1. 轄下各區總和・各分行績效與月/年增減總覽</button>
            <button type="button" class="sub-tab" data-wtab="trend-mom-yoy">📈 2. 去年至今 (2025/01~2026/11) 趨勢與增減分析</button>
            <button type="button" class="sub-tab" data-wtab="region-group" id="tabBtnRegion">🗺️ 3. 各業務分區 × 組別表現對照詳表</button>
            <button type="button" class="sub-tab" data-wtab="branch-inside" id="tabBtnInside">🔍 4. 分行內部狀況檢視 (科別/行員/客戶/案件)</button>
            <button type="button" class="sub-tab" data-wtab="pipeline">🔥 5. 重大未結追蹤案 (Pipeline) 督導</button>
          </div>

          <!-- ==================== 視角 1：轄下各分行績效與月/年增減總覽 ==================== -->
          <div class="war-panel active" id="wpanel-branch-overview">
            <!-- 表一 & 表二 長條圖檢視層級切換列 (各分行 5 家拉 BAR vs 4 大業務分區總和 vs 5 大組別總和) -->
            <div class="control-strip" id="overviewChartModeBar" style="margin-bottom:10px;background:#eef5fc">
              <label>📊 表一＆表二柱狀圖檢視層級：</label>
              <div class="metric-pill-group" id="topBarChartScopePills">
                <button type="button" class="metric-pill active" data-bscope="BRANCH_5">🏦 轄下各分行排行（每次 5 家 ＋ 拉 BAR 滑動）</button>
                <button type="button" class="metric-pill" data-bscope="REGION_SUM" id="pillScopeRegionSum">🗺️ 全行 4 大業務分區總和（北區／桃竹苗區／中區／南區）</button>
                <button type="button" class="metric-pill" data-bscope="GROUP_SUM">🏢 5 大規模組別總和（第一組～第五組）</button>
              </div>
            </div>

            <div class="chartgrid">
              <div class="card" style="margin-bottom:0">
                <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:4px">
                  <b id="chart1Title">🏦 表一：各分行「存款／授信／基金餘額」對比（每次顯示 5 家，單位：萬）</b>
                  <span class="demo" id="sliderT1RangeText">第 1 ～ 5 名 / 共 108 家</span>
                </div>
                <div class="chartbox" id="chartBranchBalances"></div>
                <!-- 表一 拉 BAR 控制器 -->
                <div class="slider-bar-wrap" id="sliderWrapT1">
                  <button type="button" class="slider-btn" id="btnT1Prev5" title="往前 5 家">⏮ -5</button>
                  <button type="button" class="slider-btn" id="btnT1Prev1" title="往前 1 家">◀</button>
                  <span style="font-size:12px;font-weight:800;color:var(--nav)">拉 BAR 檢視其他分行：</span>
                  <input type="range" id="sliderT1" min="0" max="103" step="1" value="0">
                  <button type="button" class="slider-btn" id="btnT1Next1" title="往後 1 家">▶</button>
                  <button type="button" class="slider-btn" id="btnT1Next5" title="往後 5 家">+5 ⏭</button>
                  <label style="font-size:12px;font-weight:700;color:#284b6e;display:inline-flex;align-items:center;gap:4px;cursor:pointer">
                    <input type="checkbox" id="syncSlidersChk" checked style="width:auto">同步表二與下方比較圖
                  </label>
                  <button type="button" class="chart-zoom-btn" data-zoom-chart="chartBranchBalances" style="margin-left:auto" title="放大檢視此圖表">🔍 放大檢視</button>
                </div>
              </div>

              <div class="card" style="margin-bottom:0">
                <div style="display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:4px">
                  <b id="chart2Title">🚀 表二：各分行「通報商機 vs 實際成案金額」對比（每次顯示 5 家，單位：萬）</b>
                  <span class="demo amber" id="sliderT2RangeText">第 1 ～ 5 名 / 共 108 家</span>
                </div>
                <div class="chartbox" id="chartBranchConversion"></div>
                <!-- 表二 拉 BAR 控制器 -->
                <div class="slider-bar-wrap" id="sliderWrapT2">
                  <button type="button" class="slider-btn" id="btnT2Prev5" title="往前 5 家">⏮ -5</button>
                  <button type="button" class="slider-btn" id="btnT2Prev1" title="往前 1 家">◀</button>
                  <span style="font-size:12px;font-weight:800;color:var(--nav)">拉 BAR 檢視其他分行：</span>
                  <input type="range" id="sliderT2" min="0" max="103" step="1" value="0">
                  <button type="button" class="slider-btn" id="btnT2Next1" title="往後 1 家">▶</button>
                  <button type="button" class="slider-btn" id="btnT2Next5" title="往後 5 家">+5 ⏭</button>
                  <button type="button" class="chart-zoom-btn" data-zoom-chart="chartBranchConversion" style="margin-left:auto" title="放大檢視此圖表">🔍 放大檢視</button>
                </div>
              </div>
            </div>

            <!-- ==================== 升級：多單位／多分行【對應業務餘額柱狀圖 ＋ 月增減 MoM / 年增減 YoY 折線圖】聯合比較專區 ==================== -->
            <div class="card" style="margin-top:12px;margin-bottom:0;border:1.5px solid #b8d4f2;background:#fbfdff">
              <div class="title" style="margin-bottom:8px">
                <span>📊 業務項目深度比較：【對應業務餘額／實績柱狀圖】×【月增減率 MoM% ／ 年增減率 YoY% 折線圖】</span>
                <span class="demo" id="multiLineInfoBadge">同時檢視對應業務之實際餘額柱狀圖與成長率折線</span>
              </div>

              <!-- 控制列 1：選擇比較業務指標 (存款 / 授信 / 基金 / 通報 / 成案 / 權重 / 貢獻) + 增減模式 (MoM / YoY / 實績) -->
              <div class="control-strip" style="margin-bottom:8px;background:#eef5fc">
                <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
                  <label>1️⃣ 選擇比較業務項目：</label>
                  <div class="metric-pill-group" id="lineMetricPills">
                    <button type="button" class="metric-pill active" data-metric="dep">💰 存款餘額 (表一)</button>
                    <button type="button" class="metric-pill" data-metric="loan">🤝 授信餘額 (表一)</button>
                    <button type="button" class="metric-pill" data-metric="fund">📈 基金餘額 (表一)</button>
                    <button type="button" class="metric-pill" data-metric="rep">📢 通報金額 (表二)</button>
                    <button type="button" class="metric-pill" data-metric="cls">✅ 成案金額 (表二)</button>
                    <button type="button" class="metric-pill" data-metric="weight">🏆 權重積分 (表二)</button>
                    <button type="button" class="metric-pill" data-metric="contrib">🌟 綜合貢獻 (雙表)</button>
                  </div>
                </div>

                <div style="display:flex;align-items:center;gap:8px;margin-left:auto;flex-wrap:wrap">
                  <label>2️⃣ 折線圖成長率模式：</label>
                  <select id="lineModeSelect" style="border-color:#2878e5;color:#082d5b">
                    <option value="MOM">📊 月增減率 MoM (%) ＋ 對應業務餘額柱狀圖</option>
                    <option value="YOY">📅 年增減率 YoY (%) ＋ 對應業務餘額柱狀圖</option>
                    <option value="RAW">💵 逐月實際餘額/積分趨勢 ＋ 對應業務餘額柱狀圖</option>
                  </select>
                </div>
              </div>

              <!-- 控制列 2：選擇要放在一起比較的對象 (5家拉BAR分行 / 4大業務分區總和 / 5大組別總和 / 自訂勾選多家分行) -->
              <div class="control-strip" style="margin-bottom:10px;background:#f7fafe">
                <label>3️⃣ 同圖比較對象來源：</label>
                <select id="lineBranchSourceMode">
                  <option value="SYNC_SLIDER">🔗 自動帶入上方「拉 BAR」目前顯示的 5 家分行</option>
                  <option value="REGIONS_ALL" id="optLineSourceRegions">🗺️ 全行 4 大業務分區總和（北區／桃竹苗區／中區／南區）</option>
                  <option value="GROUPS_ALL">🏢 5 大規模組別總和（第一組～第五組）</option>
                  <option value="CUSTOM">☑️ 自訂勾選多家分行同圖比較（可跨區/跨組任選）</option>
                </select>
                <label style="font-size:12px;font-weight:700;color:#193653;display:inline-flex;align-items:center;gap:4px;cursor:pointer">
                  <input type="checkbox" id="showComboBarsInTimeline" checked style="width:auto">在右側逐月折線圖底部同時顯示「各月餘額柱狀圖」
                </label>
                <span class="sub" id="lineComparedBranchesSummary" style="font-weight:700;color:#0d509c;margin-left:auto"></span>

                <div id="customBranchPickerToggleWrap" style="display:none;width:100%;margin-top:4px">
                  <div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap">
                    <input type="text" id="customBranchSearchInput" placeholder="🔎 篩選欲勾選之分行代號或名稱..." style="width:210px">
                    <button type="button" class="slider-btn" id="btnPickTop5">選取前 5 名</button>
                    <button type="button" class="slider-btn" id="btnPickTop10">選取前 10 名</button>
                    <button type="button" class="slider-btn" id="btnPickAllAllowed">全選轄下分行</button>
                    <button type="button" class="slider-btn" id="btnPickSlider5">帶入目前拉 BAR 5 家</button>
                    <button type="button" class="slider-btn" id="btnClearPicked">清除重選</button>
                    <span class="sub">（可勾選任意多家分行；超過 5 家時，圖表窗格維持顯示 5 家，並可由下方拉 BAR 拖曳檢視）</span>
                  </div>
                  <div class="branch-chip-list" id="customBranchChipContainer"></div>
                </div>
              </div>

              <!-- 並排雙圖：左圖為「純餘額柱狀圖 (去年同月 vs 上月 vs 當月，不連折線，窗格維持 5 家)」，右圖為「逐月成長率折線 + 各月餘額柱狀圖 (窗格維持 6 個月份 + 拉 BAR)」 -->
              <div class="chartgrid" style="margin-bottom:8px">
                <div class="card" style="margin-bottom:0;padding:12px;background:#fff">
                  <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:4px">
                    <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
                      <span style="font-size:13.5px;font-weight:900;color:var(--nav)">📊</span>
                      <select id="inlineBarMetricSelect" style="width:auto;padding:3px 8px;font-size:13px;font-weight:900;color:#082d5b;border:1.5px solid #2878e5;border-radius:6px;background:#eef5fc;cursor:pointer" title="點擊切換欲檢視之業務項目">
                        <option value="dep">【總存款餘額 (表一)】</option>
                        <option value="loan">【總授信餘額 (表一)】</option>
                        <option value="fund">【基金餘額 (表一)】</option>
                        <option value="rep">【通報商機金額 (表二)】</option>
                        <option value="cls">【實際成案金額 (表二)】</option>
                        <option value="weight">【階段權重積分 (表二)】</option>
                        <option value="contrib">【綜合總貢獻 (雙表)】</option>
                      </select>
                      <b id="comboBarChartTitle" style="font-size:13px;color:var(--nav)">餘額／實績柱狀圖（去年同月／上月／當月）</b>
                    </div>
                    <span class="demo green" id="comboBarUnitBadge">單位：萬（窗格維持 5 家）</span>
                  </div>
                  <div class="chartbox" id="chartMultiBranchBar" style="height:255px"></div>
                  <!-- 左圖下方：分行拉 BAR 拖曳控制器（維持圖表窗格內永遠只有 5 家） -->
                  <div class="slider-bar-wrap" id="compareSliderWrap" style="margin-top:8px;background:#eef5fc;border-color:#9ec5ff">
                    <button type="button" class="slider-btn" id="btnCmpPrev5" title="往前 5 家">⏮ -5</button>
                    <button type="button" class="slider-btn" id="btnCmpPrev1" title="往前 1 家">◀</button>
                    <span style="font-size:12px;font-weight:800;color:var(--nav)">↔️ 分行拉 BAR（窗格維持 5 家）：</span>
                    <input type="range" id="sliderCompare" min="0" max="10" step="1" value="0">
                    <button type="button" class="slider-btn" id="btnCmpNext1" title="往後 1 家">▶</button>
                    <button type="button" class="slider-btn" id="btnCmpNext5" title="往後 5 家">+5 ⏭</button>
                    <span class="demo" id="compareSliderRangeText" style="font-size:11px">第 1～5 家</span>
                    <button type="button" class="chart-zoom-btn" data-zoom-chart="chartMultiBranchBar" style="margin-left:auto" title="放大檢視此圖表">🔍 放大檢視</button>
                  </div>
                </div>

                <div class="card" style="margin-bottom:0;padding:12px;background:#fff">
                  <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:4px">
                    <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
                      <span style="font-size:13.5px;font-weight:900;color:var(--nav)">📈</span>
                      <select id="inlineLineMetricSelect" style="width:auto;padding:3px 8px;font-size:13px;font-weight:900;color:#082d5b;border:1.5px solid #2878e5;border-radius:6px;background:#eef5fc;cursor:pointer" title="點擊切換欲檢視之業務項目">
                        <option value="dep">【總存款餘額 (表一)】</option>
                        <option value="loan">【總授信餘額 (表一)】</option>
                        <option value="fund">【基金餘額 (表一)】</option>
                        <option value="rep">【通報商機金額 (表二)】</option>
                        <option value="cls">【實際成案金額 (表二)】</option>
                        <option value="weight">【階段權重積分 (表二)】</option>
                        <option value="contrib">【綜合總貢獻 (雙表)】</option>
                      </select>
                      <b id="comboLineChartTitle" style="font-size:13px;color:var(--nav)">逐月月增減率 MoM (%) 折線 ＋ 各月餘額柱狀圖</b>
                    </div>
                    <span class="demo" id="comboLineUnitBadge">窗格維持 6 個月份</span>
                  </div>
                  <div class="chartbox" id="chartMultiBranchLine" style="height:255px"></div>
                  <!-- 右圖下方：月份區間拉 BAR 拖曳控制器（維持圖表窗格內永遠只有 6 個月份） -->
                  <div class="slider-bar-wrap" id="monthSliderWrap" style="margin-top:8px;background:#eef5fc;border-color:#9ec5ff">
                    <button type="button" class="slider-btn" id="btnMonPrev6" title="往前 6 個月">⏮ -6月</button>
                    <button type="button" class="slider-btn" id="btnMonPrev1" title="往前 1 個月">◀</button>
                    <span style="font-size:12px;font-weight:800;color:var(--nav)">📅 月份拉 BAR（窗格維持 6 個月）：</span>
                    <input type="range" id="sliderLineMonths" min="0" max="16" step="1" value="16">
                    <button type="button" class="slider-btn" id="btnMonNext1" title="往後 1 個月">▶</button>
                    <button type="button" class="slider-btn" id="btnMonNext6" title="往後 6 個月">+6月 ⏭</button>
                    <span class="demo amber" id="monthSliderRangeText" style="font-size:11px">2026-06 ～ 2026-11</span>
                    <button type="button" class="chart-zoom-btn" data-zoom-chart="chartMultiBranchLine" style="margin-left:auto" title="放大檢視此圖表">🔍 放大檢視</button>
                  </div>
                </div>
              </div>

              <!-- 當前比較對象在該業務指標下的當月餘額 / 上月餘額 / MoM / 去年同月餘額 / YoY 對照表 -->
              <div class="table-wrap" style="margin-top:6px;max-height:225px">
                <table class="data-table" id="multiBranchCompareDetailTable">
                  <thead>
                    <tr>
                      <th>同圖比較單位（分區總和／分行）</th>
                      <th>歸屬分區 / 組別 / 規模</th>
                      <th id="thCurMetric">當月餘額/實績 (2026-11)</th>
                      <th id="thMomBase">上月餘額/實績 (2026-10)</th>
                      <th>月增減額</th>
                      <th>月增減率 (MoM %)</th>
                      <th id="thYoyBase">去年同月 (2025-11)</th>
                      <th>年增減額</th>
                      <th>年增減率 (YoY %)</th>
                    </tr>
                  </thead>
                  <tbody></tbody>
                </table>
              </div>
            </div>

            <div style="margin-top:14px">
              <div class="title">
                <span>🏆 轄下各分行業務表現暨【月增減 MoM / 年增減 YoY】考核總表（共 <span id="branchCountBadge">108</span> 家分行，點擊任一分行可直達「分行內部狀況檢視」）</span>
              </div>
              <div class="table-wrap">
                <table class="data-table" id="branchScorecardTable">
                  <thead>
                    <tr>
                      <th>排名</th>
                      <th>分行代號/名稱</th>
                      <th>業務分區 / 小分區 / 組別</th>
                      <th>表一：總存款 (MoM / YoY)</th>
                      <th>表一：總授信 (MoM / YoY)</th>
                      <th>表一：基金餘額 (MoM / YoY)</th>
                      <th>表一：網銀GEB率</th>
                      <th>表二：當月訪/報/成/追</th>
                      <th>表二：通報金額 (MoM)</th>
                      <th>表二：成案金額 (MoM / YoY)</th>
                      <th>表二：階段權重積分 (MoM)</th>
                      <th>綜合總貢獻 (YoY)</th>
                    </tr>
                  </thead>
                  <tbody></tbody>
                </table>
              </div>
            </div>
          </div>

          <!-- ==================== 視角 2：2025/01~2026/11 歷史趨勢與月/年增減分析 ==================== -->
          <div class="war-panel" id="wpanel-trend-mom-yoy">
            <div class="chartgrid">
              <div class="card" style="margin-bottom:0">
                <b>📈 表一：2025/01 ～ 2026/11 轄下「存款／授信／基金餘額」23個月趨勢（單位：百萬）</b>
                <div class="chartbox" id="chartHistoryT1"></div>
              </div>
              <div class="card" style="margin-bottom:0">
                <b>🚀 表二：2025/01 ～ 2026/11 轄下「通報金額 vs 成案金額」23個月趨勢（單位：百萬）</b>
                <div class="chartbox" id="chartHistoryT2"></div>
              </div>
            </div>
            <div style="margin-top:14px">
              <b>📅 2025年01月 ～ 2026年11月 逐月歷史實績與月增減 (MoM) / 年增減 (YoY) 明細表</b>
              <div class="table-wrap" style="margin-top:6px">
                <table class="data-table" id="monthlyHistoryTable">
                  <thead>
                    <tr>
                      <th>年月</th>
                      <th>表一：總存款餘額 (MoM / YoY)</th>
                      <th>表一：總授信餘額 (MoM / YoY)</th>
                      <th>表一：總基金餘額 (MoM / YoY)</th>
                      <th>表二：拜訪 / 通報 / 成案 / 追蹤</th>
                      <th>表二：通報總金額 (MoM)</th>
                      <th>表二：實際成案金額 (MoM / YoY)</th>
                      <th>表二：階段權重積分</th>
                      <th>表二：專案點數</th>
                      <th>當月綜合貢獻 (YoY)</th>
                    </tr>
                  </thead>
                  <tbody></tbody>
                </table>
              </div>
            </div>
          </div>

          <!-- ==================== 視角 3：各業務分區 × 組別表現對照 ==================== -->
          <div class="war-panel" id="wpanel-region-group">
            <div class="chartgrid">
              <div class="card" style="margin-bottom:0">
                <b>🗺️ 各業務分區（北一／北二／桃竹苗／中區／南區）存款、授信與成案對比（單位：百萬）</b>
                <div class="chartbox" id="chartRegionCompare"></div>
              </div>
              <div class="card" style="margin-bottom:0">
                <b>🏢 各規模組別（第一組～第五組）通報商機 vs 實際成案對比（單位：百萬）</b>
                <div class="chartbox" id="chartGroupCompare"></div>
              </div>
            </div>
            <div style="margin-top:14px">
              <b>🗺️ 各業務分區與規模組別【當月實績 × 月增減 MoM × 年增減 YoY】彙總比較表</b>
              <div class="table-wrap" style="margin-top:6px">
                <table class="data-table" id="regionSummaryTable">
                  <thead>
                    <tr>
                      <th>分區 / 組別維度</th>
                      <th>分行家數</th>
                      <th>管轄客戶數</th>
                      <th>表一：總存款 (MoM / YoY)</th>
                      <th>表一：總授信 (MoM / YoY)</th>
                      <th>表一：總基金 (MoM / YoY)</th>
                      <th>表一：GEB申辦率</th>
                      <th>表二：訪/報/成/追</th>
                      <th>表二：通報金額</th>
                      <th>表二：成案金額 (MoM / YoY)</th>
                      <th>表二：階段權重積分</th>
                      <th>綜合總貢獻 (YoY)</th>
                    </tr>
                  </thead>
                  <tbody></tbody>
                </table>
              </div>
            </div>
          </div>

          <!-- ==================== 視角 4：分行內部狀況檢視 (科別/行員/客戶/案件) ==================== -->
          <div class="war-panel" id="wpanel-branch-inside">
            <div class="control-strip" style="background:#eef6ff;border-color:#9ec5ff">
              <label>🏢 目前檢視內部狀況之目標分行：</label>
              <select id="insideBranchSelect" style="min-width:280px"></select>
              <span id="insideBranchMeta" class="demo"></span>
            </div>

            <!-- 該分行單獨的 MoM / YoY 摘要卡 -->
            <div class="fields-4" style="margin-bottom:12px" id="insideBranchKpiRow"></div>

            <div class="chartgrid">
              <div class="card" style="margin-bottom:0">
                <b>🏢 該分行內部三大科別（營業科／授信科／理財科）通報 vs 成案實績（單位：萬）</b>
                <div class="chartbox" id="chartInsideDepts"></div>
              </div>
              <div class="card" style="margin-bottom:0">
                <b>🧑‍💼 該分行內部各行員爭攬戰力（通報金額 vs 成案金額，單位：萬）</b>
                <div class="chartbox" id="chartInsideClerks"></div>
              </div>
            </div>

            <div class="grid" style="margin-top:12px">
              <div>
                <p class="sub" style="font-weight:800;color:var(--nav);margin:0 0 6px">🏦 該分行內部：轄下客戶每日狀態明細（表一，點擊可跳轉客戶概況）</p>
                <div class="table-wrap">
                  <table class="data-table" id="drillT1Table">
                    <thead>
                      <tr>
                        <th>客戶代號/名稱</th>
                        <th>全銜</th>
                        <th>台幣存款</th>
                        <th>授信動用/額度</th>
                        <th>基金餘額</th>
                        <th>網銀GEB</th>
                        <th>貢獻</th>
                      </tr>
                    </thead>
                    <tbody></tbody>
                  </table>
                </div>
              </div>
              <div>
                <p class="sub" style="font-weight:800;color:var(--nav);margin:0 0 6px">🚀 該分行內部：行員爭攬與後續推動紀錄（表二，點擊可編輯推動進度）</p>
                <div class="table-wrap">
                  <table class="data-table" id="drillT2Table">
                    <thead>
                      <tr>
                        <th>案件編號</th>
                        <th>科別/行員</th>
                        <th>客戶</th>
                        <th>業務</th>
                        <th>通報金額</th>
                        <th>狀態</th>
                        <th>成案金額</th>
                        <th>權重/點數</th>
                        <th>推動進度說明</th>
                      </tr>
                    </thead>
                  </table>
                  <table class="data-table" id="drillT2TableBodyOnly" style="border-top:none"><tbody></tbody></table>
                </div>
              </div>
            </div>
          </div>

          <!-- ==================== 視角 5：重大未結追蹤案 (Pipeline) 督導 ==================== -->
          <div class="war-panel" id="wpanel-pipeline">
            <div class="status">
              🔔 <b>權責追蹤案督導說明</b>：以下自動依據您目前的權責範圍（總處／各區中心／分行長官），篩選轄下於表二中<b>「已通報商機但尚未成案（成案狀態 = 追蹤）」</b>之案件，依通報金額由大至小排序。點擊任一列可直接進入案件編輯。
            </div>
            <div class="table-wrap">
              <table class="data-table" id="pipelineTable">
                <thead>
                  <tr>
                    <th>優先序</th>
                    <th>所屬分行 (分區/組別)</th>
                    <th>主辦科別 / 行員</th>
                    <th>案件編號 / 月份</th>
                    <th>爭攬客戶</th>
                    <th>通報業務</th>
                    <th>通報金額</th>
                    <th>狀態</th>
                    <th>階段權重</th>
                    <th>後續推動進度說明</th>
                    <th>協作單位</th>
                    <th>後續行動與期限</th>
                  </tr>
                </thead>
                <tbody></tbody>
              </table>
            </div>
          </div>
        </div>
      </section>

      <!-- ==================== PAGE 2: 客戶概況 (表一 + 表二關聯) ==================== -->
      <section class="page" id="page-customer">
        <!-- 頂部雙表連動切換器 -->
        <div class="selector-bar" style="margin-bottom:12px">
          <div class="selector-group">
            <label>🏦 表一：選擇轄下客戶</label>
            <select id="customerSelect"></select>
          </div>
          <div class="selector-group">
            <label>📋 表二：該戶爭攬案件</label>
            <select id="caseSelect"></select>
          </div>
          <button class="btn primary" id="newCaseBtn">➕ 新增此客戶爭攬紀錄</button>
        </div>

        <div class="grid">
          <div class="card">
            <div class="title">
              <span>客戶基本資料 <span class="demo">來源：表一《客戶每日狀態表》</span></span>
              <span id="custDateBadge" class="sub">資料月份：2026-11</span>
            </div>
            <div class="fields">
              <div class="field"><label>客戶代號 / 代稱</label><input id="custCodeName" readonly></div>
              <div class="field"><label>客戶全銜</label><input id="cust"></div>
              <div class="field"><label>統一編號</label><input id="uni"></div>
              <div class="field">
                <label>產業別</label>
                <select id="industry">
                  <option>生技醫療業</option>
                  <option>製造業</option>
                  <option>科技業</option>
                  <option>服務業</option>
                  <option>傳統產業</option>
                </select>
              </div>
              <div class="field">
                <label>內部信評等級</label>
                <select id="rating">
                  <option>5</option>
                  <option>6</option>
                  <option>7</option>
                  <option>8</option>
                </select>
              </div>
              <div class="field"><label>歸屬分區 / 組別 / 分行 (等級)</label><input id="custBranchInfo" readonly></div>
              <div class="field"><label>公司電話</label><input id="custPhone"></div>
              <div class="field"><label>主責行員代號</label><input id="custRM"></div>
              <div class="field full"><label>公司地址</label><input id="custAddr"></div>
            </div>
            <p class="sub" style="margin:10px 0 4px;font-weight:700">🤖 上次拜訪 AI 洽談摘要（表一日結備註）</p>
            <div class="summary" id="aiSummaryBox"></div>
          </div>

          <div class="card">
            <div class="title">
              <span>本行每日往來狀況 <span class="demo">來源：表一《客戶每日狀態表》</span></span>
              <span id="gebBadge" class="demo green">企業網銀 GEB：已申辦</span>
            </div>
            <div class="products">
              <div class="product">
                <b>💰 台幣存款餘額</b>
                <div class="val" id="pDeposit">NT$ 0</div>
                <span class="sub" id="pDepositRaw"></span>
              </div>
              <div class="product">
                <b>💵 外幣存款餘額</b>
                <div class="val" id="pFxDeposit">NT$ 0</div>
                <span class="sub" id="pFxDepositRaw"></span>
              </div>
              <div class="product">
                <b>🤝 授信動用 ／ 額度</b>
                <div class="val" id="pLoan">0 / 0</div>
                <span class="sub" id="pLoanRate">動用率 0%</span>
              </div>
              <div class="product">
                <b>📈 基金餘額 (本月新購)</b>
                <div class="val" id="pFund">NT$ 0</div>
                <span class="sub" id="pFundMonth">本月購買：0</span>
              </div>
              <div class="product">
                <b>🌐 企業網銀 (GEB) & 薪轉</b>
                <div class="val" id="pGeb">已申辦</div>
                <span class="sub" id="pPayroll">薪轉戶：已申辦</span>
              </div>
              <div class="product">
                <b>🌟 客戶總貢獻度 & 外匯</b>
                <div class="val" id="pContrib">100</div>
                <span class="sub" id="pFxTrade">匯兌/進出口</span>
              </div>
            </div>

            <div class="title" style="margin-top:14px">
              <span>當前案件商機設定 <span class="demo amber">連動表二爭攬紀錄</span></span>
            </div>
            <div class="check" id="opportunities">
              <label><input type="checkbox" value="授信">授信</label>
              <label><input type="checkbox" value="存款">存款</label>
              <label><input type="checkbox" value="理財">理財</label>
              <label><input type="checkbox" value="外幣存款">外幣存款</label>
              <label><input type="checkbox" value="匯兌">匯兌</label>
              <label><input type="checkbox" value="進出口">進出口</label>
              <label><input type="checkbox" value="網銀GEB">網銀GEB</label>
            </div>
            <div class="fields" style="margin-top:8px">
              <div class="field">
                <label>通報商機金額（如 3000萬、10億）</label>
                <input id="amount" type="text" value="3000萬">
              </div>
              <div class="field">
                <label>實際成案金額（如 2000萬、10億）</label>
                <input id="closedAmount" type="text" value="2000萬">
              </div>
            </div>
            <div class="metric" style="display:flex;justify-content:space-between;align-items:center">
              <div>
                <span class="m-lbl">通報商機換算金額</span>
                <b class="m-val" id="oppValue">NT$ 30,000,000</b>
              </div>
              <div style="text-align:right">
                <span class="m-lbl">成案換算金額</span>
                <b class="m-val" id="closedValue" style="color:var(--green)">NT$ 20,000,000</b>
              </div>
            </div>
          </div>

          <div class="card full">
            <div class="title">
              <span>📋 該客戶之行員爭攬與後續推動紀錄清單 <span class="demo">來源：表二《行員爭攬業務紀錄表》</span></span>
              <span class="sub">點擊任一列可切換檢視或至「業務爭攬與推動」分頁編輯</span>
            </div>
            <div class="table-wrap">
              <table class="data-table" id="custCasesTable">
                <thead>
                  <tr>
                    <th>案件編號</th>
                    <th>月份</th>
                    <th>分區/組別/分行</th>
                    <th>科別</th>
                    <th>爭攬行員</th>
                    <th>訪客方式</th>
                    <th>通報</th>
                    <th>通報業務</th>
                    <th>通報金額</th>
                    <th>成案狀態</th>
                    <th>成案金額</th>
                    <th>點數(說明)</th>
                    <th>階段權重積分</th>
                    <th>案件貢獻</th>
                    <th>推動進度說明</th>
                  </tr>
                </thead>
                <tbody></tbody>
              </table>
            </div>
          </div>

          <div class="card full">
            <div class="title">🛡️ AI 數據守門員（雙資料表交叉檢核 & 外部資料源狀態）</div>
            <div class="status" id="guardianCrossCheck">正在執行表一《客戶每日狀態》與表二《行員爭攬紀錄》交叉檢核...</div>
            <button class="btn" id="guardianBtn">檢視外部比對來源連線狀態</button>
            <div id="sources" class="sub" style="display:none;margin-top:8px">
              經濟部工商資料：未連線；工廠登記：未連線；聯徵/資保資料源：未連線。外部比對須串接核准資料服務，目前僅就「表一（行內客戶日結狀態）」與「表二（行員爭攬紀錄）」進行內部一致性勾稽。
            </div>
          </div>
        </div>
      </section>

      <!-- ==================== PAGE 3: 業務爭攬與推動 (表二) ==================== -->
      <section class="page" id="page-interview">
        <div class="grid">
          <div class="card">
            <div class="title">
              <span>行員爭攬業務紀錄與後續推動情形 <span class="demo amber">寫入：表二《行員爭攬業務紀錄表》</span></span>
              <span id="currentCaseBadge" class="demo">CASE-202611-001</span>
            </div>

            <div class="weight-pill">
              <b>📊 業務推動階段權重：</b>
              <span class="weight-step on" id="stepVisit">1. 拜訪 (+0.2)</span>
              <span>➔</span>
              <span class="weight-step" id="stepReport">2. 通報 (+0.3)</span>
              <span>➔</span>
              <span class="weight-step" id="stepClose">3. 成案 (+0.5)</span>
              <span style="margin-left:auto;font-weight:900;color:var(--nav)" id="totalWeightText">合計積分：1.0</span>
            </div>

            <div class="fields-4" style="margin-top:8px">
              <div class="field"><label>資料月份</label><input id="fDate" value="2026-11"></div>
              <div class="field"><label>行員代號</label><input id="fClerkId" value="1234"></div>
              <div class="field"><label>行員姓名</label><input id="fClerkName" value="陳建宏"></div>
              <div class="field">
                <label>科別</label>
                <select id="fDept">
                  <option value="營業">營業</option>
                  <option value="授信">授信</option>
                  <option value="理財">理財</option>
                </select>
              </div>
              <div class="field">
                <label>業務分區</label>
                <select id="fRegion">
                  <option value="北一區">北一區</option>
                  <option value="北二區">北二區</option>
                  <option value="桃竹苗區">桃竹苗區</option>
                  <option value="中區">中區</option>
                  <option value="南區">南區</option>
                </select>
              </div>
              <div class="field">
                <label>組別</label>
                <select id="fGroup">
                  <option value="第一組">第一組</option>
                  <option value="第二組">第二組</option>
                  <option value="第三組">第三組</option>
                  <option value="第四組">第四組</option>
                  <option value="第五組">第五組</option>
                </select>
              </div>
              <div class="field"><label>分行代號/名稱</label><input id="fBranch" value="002 港都分行"></div>
              <div class="field">
                <label>訪客方式</label>
                <select id="fVisitType">
                  <option value="約訪">約訪</option>
                  <option value="臨櫃">臨櫃</option>
                  <option value="電訪">電訪</option>
                </select>
              </div>
            </div>

            <div class="fields-4" style="margin-top:8px">
              <div class="field">
                <label>是否通報商機</label>
                <select id="fHasReport">
                  <option value="有">有 (+0.3)</option>
                  <option value="無">無 (0)</option>
                </select>
              </div>
              <div class="field">
                <label>成案推動狀態</label>
                <select id="fCloseStatus">
                  <option value="有">有 - 已成案 (+0.5)</option>
                  <option value="追蹤">追蹤 - 推動中 (0)</option>
                  <option value="無">無 - 未成案 (0)</option>
                </select>
              </div>
              <div class="field"><label>專案點數 (如 GEB)</label><input id="fPoints" type="number" value="0"></div>
              <div class="field"><label>點數說明</label><input id="fPointsNote" placeholder="如：GEB申請"></div>
            </div>

            <div class="fields" style="margin-top:8px">
              <div class="field">
                <label>後續推動進度說明（最新核准、送審或追蹤情形）</label>
                <input id="fProgressNote" placeholder="請輸入業務後續推動情形...">
              </div>
              <div class="field">
                <label>案件貢獻值</label>
                <input id="fCaseContrib" type="number" value="100">
              </div>
            </div>

            <hr style="border:none;border-top:1px solid var(--line);margin:12px 0">

            <label style="font-size:12px;font-weight:700;color:#50677d;display:block;margin-bottom:4px">客戶營收狀況</label>
            <div class="row" id="revBtns" style="margin-bottom:8px">
              <button type="button" class="btn primary" data-rev="成長">成長</button>
              <button type="button" class="btn" data-rev="持平">持平</button>
              <button type="button" class="btn" data-rev="衰退">衰退</button>
              <button type="button" class="btn" data-rev="其他">其他</button>
            </div>

            <div class="fields">
              <div class="field"><label>預估成長幅度（%）</label><input id="growth" type="number" value="15"></div>
              <div class="field">
                <label>加班頻率</label>
                <select id="shift">
                  <option>三班</option>
                  <option>二班</option>
                  <option>一班</option>
                  <option>其他</option>
                </select>
              </div>
            </div>

            <div class="field" style="margin-top:8px"><label>訪談重點紀錄（補充說明）</label><textarea id="operation"></textarea></div>
            <div class="field" style="margin-top:8px"><label>風險與需求</label><textarea id="risk"></textarea></div>
            <div class="fields" style="margin-top:8px">
              <div class="field"><label>後續行動</label><input id="action"></div>
              <div class="field"><label>後續行動期限</label><input id="due" type="date"></div>
            </div>

            <div class="row" style="margin-top:12px">
              <button class="btn success" id="saveToTable2Btn">💾 儲存／更新至此筆表二紀錄</button>
              <button class="btn primary" id="summaryBtn">🔄 整理摘要預覽</button>
              <button class="btn" id="save">本機暫存草稿</button>
            </div>
            <div class="summary" id="visitSummary" style="margin-top:8px">尚未整理摘要</div>
          </div>

          <div>
            <div class="card">
              <div class="title">
                <span>訪談問題檢核清單</span>
                <span id="qCount" class="demo">0 / 10 已完成</span>
              </div>
              <div class="check block" id="questions">
                <label><input type="checkbox" checked>1. 近期營收、接單與主要市場趨勢如何？</label>
                <label><input type="checkbox" checked>2. 擴廠、設備汰換或資本支出的時程為何？</label>
                <label><input type="checkbox" checked>3. 資金需求、授信額度及動用時間為何？</label>
                <label><input type="checkbox" checked>4. 是否有外幣收付款或避險需求？</label>
                <label><input type="checkbox" checked>5. 員工福利、薪轉或企業網銀(GEB)服務有哪些需求？</label>
                <label><input type="checkbox" checked>6. 後續推動由誰追蹤，預計何時回覆？</label>
                <label><input type="checkbox" checked>7. 產線加班頻率為何？（三班／二班／一班／其他）</label>
                <label><input type="checkbox" checked>8. 表一客戶每日往來餘額與網銀狀態是否已確認？</label>
                <label><input type="checkbox">9. 表二爭攬業務通報金額、成案進度與專案點數是否已登錄？</label>
                <label><input type="checkbox">10. 通報設定：接收單位（分行／海外／協辦）是否已確認？</label>
              </div>
            </div>

            <div class="card">
              <div class="title">商情通報協作單位設定</div>
              <div class="sub">勾選協作單位（將同步寫入表二「協作單位」欄位）：</div>
              <div class="check unit" id="unitChecks">
                <label><input type="checkbox" value="授信單位" checked>授信單位</label>
                <label><input type="checkbox" value="營業單位" checked>營業單位</label>
                <label><input type="checkbox" value="理財單位">理財單位</label>
                <label><input type="checkbox" value="匯兌單位">匯兌單位</label>
                <label><input type="checkbox" value="進出口單位">進出口單位</label>
                <label><input type="checkbox" value="海外單位">海外單位</label>
                <label><input type="checkbox" value="協辦單位">協辦單位</label>
              </div>
              <div class="sub" style="margin-top:10px">海外分行（逐一勾選）</div>
              <div class="field">
                <label>海外分行名單（每行一個名稱）</label>
                <textarea id="overseasBranchNames" placeholder="例如：&#10;香港分行&#10;新加坡分行&#10;東京分行"></textarea>
              </div>
              <button class="btn" id="buildOverseasBranches" style="margin-top:6px">更新海外分行勾選項目</button>
              <div class="check" id="overseasBranches" style="margin-top:6px"></div>
            </div>
          </div>
        </div>
      </section>

      <!-- ==================== PAGE 4: 行銷報告 ==================== -->
      <section class="page" id="page-marketing">
        <div class="card">
          <div class="title">
            <span>📄 行銷拜訪暨業務推動報告 <span class="demo">自動整合：表一客戶狀態 ＋ 表二爭攬推動紀錄</span></span>
          </div>
          <div class="status">
            STE-100 導向繁體中文檢核示意，不代表官方認證。85% 是本次設定的品質門檻，自動檢核表一與表二欄位完整性。
          </div>
          <div class="fields-4 no-print">
            <div class="field"><label>報告期間／拜訪月份</label><input id="period" value="2026-11"></div>
            <div class="field"><label>報告負責人 (自動帶入爭攬行員)</label><input id="owner" value="1234 陳建宏"></div>
            <div class="field"><label>後續行動期限</label><input id="reportDue" type="date" value="2026-11-28"></div>
            <div class="field"><label>資料來源</label><input id="source" value="表一《客戶每日狀態表》＋表二《行員爭攬業務紀錄表》"></div>
          </div>
          <div class="row no-print" style="margin:12px 0">
            <button class="btn primary" id="makeReport">⚡ 產生完整雙表整合報告</button>
            <button class="btn" id="print">🖨️ 列印／另存 PDF</button>
            <b id="score" class="score">尚未檢核</b>
            <span class="sub">門檻 85%</span>
          </div>
          <div id="report" class="report">按「產生完整雙表整合報告」自動彙整表一客戶日結狀態與表二業務推動紀錄。</div>
          <div id="checks" class="sub" style="margin-top:8px"></div>
        </div>
      </section>
    </main>
  </div>

  <!-- ==================== 圖表放大檢視互動視窗 (Chart Zoom Modal) ==================== -->
  <div class="zoom-modal-backdrop" id="chartZoomModal">
    <div class="zoom-modal-card">
      <div class="zoom-modal-header">
        <div>
          <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
            <span id="zoomModalIcon" style="font-size:17px">📈</span>
            <!-- 左上角業務項目下拉式選單 (直接切換各項業務) -->
            <select id="zoomMetricSelect" style="width:auto;padding:5px 10px;font-size:14.5px;font-weight:900;color:#082d5b;background:#fff;border:2px solid #93c5fd;border-radius:7px;cursor:pointer;display:none" title="下拉選擇其他各項業務指標">
              <option value="dep">💰 【總存款餘額 (表一)】</option>
              <option value="loan">🤝 【總授信餘額 (表一)】</option>
              <option value="fund">📈 【基金餘額 (表一)】</option>
              <option value="rep">📢 【通報商機金額 (表二)】</option>
              <option value="cls">✅ 【實際成案金額 (表二)】</option>
              <option value="weight">🏆 【階段權重積分 (表二)】</option>
              <option value="contrib">🌟 【綜合總貢獻 (雙表)】</option>
            </select>
            <select id="zoomModeSelect" style="width:auto;padding:5px 10px;font-size:13.5px;font-weight:800;color:#082d5b;background:#eff6ff;border:1.5px solid #93c5fd;border-radius:7px;cursor:pointer;display:none" title="下拉切換月增減率 MoM% / 年增減率 YoY% / 實際數值">
              <option value="MOM">逐月月增減率 MoM (%) 折線 ＋ 各月餘額柱狀圖</option>
              <option value="YOY">逐月年增減率 YoY (%) 折線 ＋ 各月餘額柱狀圖</option>
              <option value="RAW">逐月實際數值趨勢折線 ＋ 各月餘額柱狀圖</option>
            </select>
            <div style="font-size:16px;font-weight:900" id="zoomModalTitle">📊 圖表放大檢視</div>
          </div>
          <div style="font-size:12px;color:#bcd7f5;margin-top:4px" id="zoomModalSubtitle">可由左上角下拉選單直接切換「各項業務類別」，並於下方拖曳拉 BAR 檢視其他分行或月份區間</div>
        </div>
        <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
          <span style="font-size:12px;font-weight:700;color:#dbeafe">檢視縮放：</span>
          <button type="button" class="slider-btn" data-zoom-scale="1">100% 大圖</button>
          <button type="button" class="slider-btn" data-zoom-scale="1.35">135% 特大</button>
          <button type="button" class="slider-btn" data-zoom-scale="1.7">170% 超清</button>
          <button type="button" class="btn" id="btnCloseZoomModal" style="background:#dc2626;color:#fff;border-color:#b91c1c;padding:6px 14px">✕ 關閉放大檢視 (ESC)</button>
        </div>
      </div>
      <div class="zoom-modal-body">
        <div class="zoom-chart-stage" id="zoomModalStage"></div>
      </div>
      <div class="zoom-modal-footer">
        <div id="zoomModalSliderControls" style="display:flex;align-items:center;gap:8px;flex:1;flex-wrap:wrap">
          <button type="button" class="slider-btn" id="btnZoomStepPrevBig">⏮</button>
          <button type="button" class="slider-btn" id="btnZoomStepPrev1">◀</button>
          <span style="font-size:12.5px;font-weight:800;color:var(--nav)" id="zoomModalSliderLabel">↔️ 拉 BAR 移動檢視：</span>
          <input type="range" id="zoomModalRangeInput" min="0" max="10" step="1" value="0" style="flex:1;min-width:180px;accent-color:#2878e5;cursor:pointer">
          <button type="button" class="slider-btn" id="btnZoomStepNext1">▶</button>
          <button type="button" class="slider-btn" id="btnZoomStepNextBig">⏭</button>
          <span class="demo" id="zoomModalRangeBadge"></span>
        </div>
        <div style="font-size:12px;color:#47627d;font-weight:700">💡 提示：將滑鼠移至柱狀圖或折線節點上可顯示詳細數值與增減率</div>
      </div>
    </div>
  </div>

  <script>
  (function() {
    var NL = String.fromCharCode(10);
    var SIM_DATA = __SIM_PAYLOAD__;

    function normalizeRegionName(rg) {
      if (rg === "北一區" || rg === "北二區") return "北區";
      return rg || "北區";
    }

    var allMonths = SIM_DATA.months; // ["2025-01", ..., "2026-11"]
    var branchMonthlyList = SIM_DATA.branchMonthly.map(function(b) {
      b.region = normalizeRegionName(b.region);
      return b;
    }); // 108 branches with 23 months of [depW, loanW, limitW, fundW, fundNewW, t1Contrib, visits, reports, closed, tracking, repW, clsW, weightX10, points, t2Contrib]

    // 將 table1 與 table2 轉換為前端使用格式
    var table1Customers = SIM_DATA.table1.map(function(r) {
      return {
        date: r["資料日期"],
        id: r["客戶代號"],
        shortName: r["客戶"],
        uni: r["統一編號"],
        fullName: r["客戶全銜"],
        industry: r["產業別"],
        rating: r["信評"],
        region: normalizeRegionName(r["業務分區"]),
        subRegion: r["小分區"],
        group: r["組別"],
        category: r["分區"],
        branch: r["分行代號"],
        branchName: r["分行名稱"],
        tier: r["分行歸屬"],
        rm: r["主責行員"],
        deposit: r["存款餘額"],
        fxDeposit: r["外幣存款餘額"],
        loanLimit: r["授信額度"],
        loanBalance: r["授信餘額"],
        fundBalance: r["基金餘額"],
        fundMonth: r["本月購買基金"],
        geb: r["是否申辦網銀(GEB)"],
        payroll: r["薪轉戶狀態"],
        fxStatus: r["匯兌往來"],
        tradeStatus: r["進出口往來"],
        contrib: Number(r["貢獻"] || 0),
        phone: r["公司電話"],
        addr: r["公司地址"],
        aiSummary: r["上次拜訪AI摘要"]
      };
    });

    var table2Records = SIM_DATA.table2.map(function(r) {
      return {
        caseId: r["案件編號"],
        ym: r["資料月份"],
        date: r["日期"],
        clerkId: r["行員"],
        clerkName: r["行員姓名"],
        dept: r["科別"],
        region: normalizeRegionName(r["業務分區"]),
        subRegion: r["小分區"],
        group: r["組別"],
        category: r["分區"],
        branch: r["分行代號"],
        branchName: r["分行名稱"],
        visitType: r["訪客"],
        custId: r["客戶代號"],
        custShort: r["客戶"],
        uni: r["統一編號"],
        tier: r["分行歸屬"],
        hasReport: r["通報"],
        bizType: r["通報業務"],
        reportAmt: r["通報金額"],
        units: r["協作單位"],
        closeStatus: r["成案"],
        progressNote: r["推動進度說明"],
        closeAmt: r["成案金額"],
        points: Number(r["點數"] || 0),
        pointsNote: r["點數說明"],
        weight: Number(r["階段權重積分"] || 0.5),
        contrib: Number(r["案件貢獻"] || 0),
        revenue: r["營收狀況"],
        growth: Number(r["預估成長幅度(%)"] || 15),
        shift: r["加班頻率"],
        operation: r["訪談重點紀錄"],
        risk: r["風險與需求"],
        action: r["後續行動"],
        due: r["行動期限"]
      };
    });

    // 權責與狀態變數
    var currentRole = "HQ"; // "HQ" | "REGION" | "BRANCH"
    var lockedRegion = "北區";
    var lockedBranch = "002";
    var selectedMonth = "2026-11";
    var insideBranchCode = "002";

    var currentCustId = table1Customers[0].id;
    var currentCaseId = table2Records[0].caseId;
    var revenue = "成長";

    function el(id) { return document.getElementById(id); }

    function toast(msg) {
      var t = el("toast");
      t.textContent = msg;
      t.style.display = "block";
      clearTimeout(t._timer);
      t._timer = setTimeout(function() { t.style.display = "none"; }, 2600);
    }

    function parseMoney(val) {
      if (val === null || val === undefined) return 0;
      var s = String(val).replace(/,/g, "").trim();
      if (!s) return 0;
      if (s.indexOf("億") !== -1) {
        var n = parseFloat(s.replace("億", ""));
        return isNaN(n) ? 0 : n * 100000000;
      }
      if (s.indexOf("萬") !== -1) {
        var m = parseFloat(s.replace("萬", ""));
        return isNaN(m) ? 0 : m * 10000;
      }
      var v = parseFloat(s);
      return isNaN(v) ? 0 : v;
    }

    function formatNT(num) {
      return "NT$ " + Math.round(num).toLocaleString("en-US");
    }

    // 輸入單位為「萬」的格式化
    function formatWanToReadable(wanVal) {
      var w = Math.round(wanVal);
      if (Math.abs(w) >= 10000) {
        return (w / 10000).toFixed(2) + " 億";
      }
      return w.toLocaleString("en-US") + " 萬";
    }

    // 計算增減率標籤 HTML (MoM / YoY)
    function deltaBadgeHtml(label, curVal, baseVal) {
      if (!baseVal || baseVal <= 0) {
        return '<span class="delta-flat">' + label + ' —</span>';
      }
      var diff = curVal - baseVal;
      var pct = ((diff / baseVal) * 100).toFixed(1);
      if (diff > 0) {
        return '<span class="delta-up">' + label + ' ▲+' + pct + '%</span>';
      } else if (diff < 0) {
        return '<span class="delta-down">' + label + ' ▼' + pct + '%</span>';
      }
      return '<span class="delta-flat">' + label + ' 0.0%</span>';
    }

    function getPrevMonth(ym) {
      var idx = allMonths.indexOf(ym);
      return idx > 0 ? allMonths[idx - 1] : null;
    }

    function getYoYMonth(ym) {
      var parts = ym.split("-");
      var prevY = (Number(parts[0]) - 1) + "-" + parts[1];
      return allMonths.indexOf(prevY) !== -1 ? prevY : null;
    }

    function calcStageWeight(hasReport, closeStatus) {
      var w = 0.2;
      if (hasReport === "有") w += 0.3;
      if (closeStatus === "有") w += 0.5;
      return Math.round(w * 10) / 10;
    }

    function selected(selector) {
      var nodes = document.querySelectorAll(selector);
      var arr = [];
      for (var i = 0; i < nodes.length; i++) if (nodes[i].checked) arr.push(nodes[i].value);
      return arr;
    }

    function setCheckedValues(selector, valuesArr) {
      var nodes = document.querySelectorAll(selector);
      for (var i = 0; i < nodes.length; i++) {
        nodes[i].checked = valuesArr.indexOf(nodes[i].value) !== -1;
      }
    }

    // =========================================================================
    // 1. 初始化下拉選單 (月份選單 + 108家分行選單)
    // =========================================================================
    function initStaticDropdowns() {
      var mSel = el("warMonthSelect");
      mSel.innerHTML = "";
      for (var i = allMonths.length - 1; i >= 0; i--) {
        var ym = allMonths[i];
        var rocY = Number(ym.slice(0, 4)) - 1911;
        var opt = document.createElement("option");
        opt.value = ym;
        opt.textContent = ym + " (民國" + rocY + "年" + ym.slice(5, 7) + "月)";
        if (ym === selectedMonth) opt.selected = true;
        mSel.appendChild(opt);
      }

      var bSel = el("rbacBranchSelect");
      bSel.innerHTML = "";
      branchMonthlyList.forEach(function(b) {
        var opt = document.createElement("option");
        opt.value = b.code;
        opt.textContent = b.code + " " + b.name + " (" + b.region + " / " + b.group + ")";
        bSel.appendChild(opt);
      });
    }

    // =========================================================================
    // 2. 權責過濾邏輯 (總處 > 各區中心 > 分行長官)
    // =========================================================================
    function getAllowedBranches() {
      var regFilter = el("warRegionFilter").value;
      var grpFilter = el("warGroupFilter").value;
      var q = (el("warBranchSearch").value || "").trim().toLowerCase();

      return branchMonthlyList.filter(function(b) {
        // 1. 強制依登入權責鎖定
        if (currentRole === "REGION" && b.region !== lockedRegion) return false;
        if (currentRole === "BRANCH" && b.code !== lockedBranch) return false;

        // 2. 戰情室篩選器
        if (currentRole === "HQ" && regFilter !== "ALL" && b.region !== regFilter) return false;
        if (grpFilter !== "ALL" && b.group !== grpFilter) return false;
        if (q && b.code.toLowerCase().indexOf(q) === -1 && b.name.toLowerCase().indexOf(q) === -1 && b.subRegion.toLowerCase().indexOf(q) === -1) {
          return false;
        }
        return true;
      });
    }

    function applyRbacUIState() {
      currentRole = el("rbacRole").value;
      lockedRegion = el("rbacRegionSelect").value;
      lockedBranch = el("rbacBranchSelect").value;
      sliderOffsetT1 = 0;
      sliderOffsetT2 = 0;

      el("rbacRegionBox").style.display = currentRole === "REGION" ? "block" : "none";
      el("rbacBranchBox").style.display = currentRole === "BRANCH" ? "block" : "none";

      // 控制篩選器與分頁顯示
      el("filterRegionWrap").style.display = currentRole === "HQ" ? "block" : "none";
      el("filterGroupWrap").style.display = currentRole === "BRANCH" ? "none" : "block";
      el("filterSearchWrap").style.display = currentRole === "BRANCH" ? "none" : "block";
      el("tabBtnRegion").style.display = currentRole === "BRANCH" ? "none" : "inline-block";
      el("hqRegionTotalsSection").style.display = currentRole === "HQ" ? "block" : "none";
      el("pillScopeRegionSum").style.display = currentRole === "HQ" ? "inline-block" : "none";
      if (el("optLineSourceRegions")) {
        el("optLineSourceRegions").disabled = currentRole !== "HQ";
      }
      if (currentRole !== "HQ" && topBarChartScope === "REGION_SUM") {
        topBarChartScope = "BRANCH_5";
      }
      if (currentRole !== "HQ" && lineBranchSource === "REGIONS_ALL") {
        lineBranchSource = "SYNC_SLIDER";
        el("lineBranchSourceMode").value = "SYNC_SLIDER";
      }

      var insideSel = el("insideBranchSelect");
      insideSel.innerHTML = "";
      var rbacBranches = branchMonthlyList.filter(function(b) {
        if (currentRole === "REGION") return b.region === lockedRegion;
        if (currentRole === "BRANCH") return b.code === lockedBranch;
        return true;
      });
      rbacBranches.forEach(function(b) {
        var o = document.createElement("option");
        o.value = b.code;
        o.textContent = b.code + " " + b.name + " (" + b.region + "・" + b.subRegion + "・" + b.group + ")";
        insideSel.appendChild(o);
      });

      if (currentRole === "HQ") {
        el("rbacStatusText").innerHTML = "目前權責：<b>【總處】</b><br>可檢核全體、4大業務分區（北區／桃竹苗區／中區／南區）、108家分行及各分行內部狀況。";
        el("topHeaderTitle").textContent = "🏦 全行業務與績效戰情室 — 【總處視角】全體・各區・108家分行檢核看板";
        if (!rbacBranches.some(function(x) { return x.code === insideBranchCode; })) {
          insideBranchCode = rbacBranches[0].code;
        }
      } else if (currentRole === "REGION") {
        el("rbacStatusText").innerHTML = "目前權責：<b>【" + lockedRegion + "中心】</b><br>已鎖定轄下 " + rbacBranches.length + " 家分行與分行內部狀況。";
        el("topHeaderTitle").textContent = "🗺️ 區域業務戰情室 — 【" + lockedRegion + "營運中心】轄下各分行與內部狀況檢核";
        insideBranchCode = rbacBranches[0].code;
      } else {
        var bObj = rbacBranches[0];
        el("rbacStatusText").innerHTML = "目前權責：<b>【" + bObj.code + " " + bObj.name + "】分行長官</b><br>已鎖定本分行內部狀況與行員表現。";
        el("topHeaderTitle").textContent = "🏢 分行業務戰情室 — 【" + bObj.code + " " + bObj.name + "】分行內部狀況與增減檢核";
        insideBranchCode = bObj.code;
        // 分行長官預設開啟「分行內部狀況」或「趨勢」
        switchWarSubTab("branch-inside");
      }
      insideSel.value = insideBranchCode;

      renderSelectors();
      loadCurrentSelectionToUI();
      drawWarRoom();
    }

    function switchWarSubTab(target) {
      var wTabs = document.querySelectorAll("#warSubTabs .sub-tab");
      for (var i = 0; i < wTabs.length; i++) {
        wTabs[i].classList.toggle("active", wTabs[i].getAttribute("data-wtab") === target);
      }
      var panels = document.querySelectorAll(".war-panel");
      for (var j = 0; j < panels.length; j++) panels[j].classList.remove("active");
      var activePanel = el("wpanel-" + target);
      if (activePanel) activePanel.classList.add("active");
    }

    // =========================================================================
    // 3. 彙總計算器 (給定分行陣列與月份，回傳該月各項指標總和)
    // =========================================================================
    function aggregateBranchesAtMonth(branchesArr, ym) {
      var res = {
        branchCount: branchesArr.length,
        custCount: 0,
        gebCount: 0,
        depW: 0,
        loanW: 0,
        limitW: 0,
        fundW: 0,
        fundNewW: 0,
        t1Contrib: 0,
        visits: 0,
        reports: 0,
        closed: 0,
        tracking: 0,
        repW: 0,
        clsW: 0,
        weight: 0,
        points: 0,
        t2Contrib: 0,
        totalContrib: 0
      };
      if (!ym) return res;
      for (var i = 0; i < branchesArr.length; i++) {
        var b = branchesArr[i];
        res.custCount += b.custCount;
        res.gebCount += b.gebCount;
        var m = b.m[ym];
        if (m) {
          res.depW += m[0];
          res.loanW += m[1];
          res.limitW += m[2];
          res.fundW += m[3];
          res.fundNewW += m[4];
          res.t1Contrib += m[5];
          res.visits += m[6];
          res.reports += m[7];
          res.closed += m[8];
          res.tracking += m[9];
          res.repW += m[10];
          res.clsW += m[11];
          res.weight += m[12] / 10.0;
          res.points += m[13];
          res.t2Contrib += m[14];
        }
      }
      res.totalContrib = res.t1Contrib + res.t2Contrib;
      return res;
    }

    var activeZoomChartId = null;
    var zoomScaleFactor = 1;

    function mountChartWithZoom(containerId, htmlContent) {
      var box = el(containerId);
      if (!box) return;
      box.innerHTML = htmlContent +
        '<button type="button" class="chart-zoom-btn chart-zoom-float" data-zoom-chart="' + containerId + '" title="點擊放大檢視此圖表">🔍 放大</button>';
      if (activeZoomChartId === containerId) {
        syncZoomModalContent();
      }
    }

    // 原生 SVG 長條圖與折線趨勢圖渲染器 (支援 5 家分行寬裕間距與柱頂數值標籤)
    function renderSvgBarChart(containerId, labels, datasets) {
      var box = el(containerId);
      if (!box) return;
      if (!labels.length) {
        box.innerHTML = '<div style="text-align:center;padding-top:80px;color:#647b92">無符合篩選條件之資料</div>';
        return;
      }
      var maxVal = 1;
      datasets.forEach(function(ds) {
        ds.data.forEach(function(v) { if (v > maxVal) maxVal = v; });
      });
      var legendHtml = '<div style="display:flex;gap:14px;justify-content:center;font-size:12px;margin-bottom:4px;flex-wrap:wrap">';
      datasets.forEach(function(ds) {
        legendHtml += '<span style="display:inline-flex;align-items:center;gap:5px"><i style="width:11px;height:11px;border-radius:3px;background:' + ds.color + ';display:inline-block"></i>' + ds.label + '</span>';
      });
      legendHtml += '</div>';

      var W = 560, H = 205, padL = 56, padR = 14, padT = 22, padB = 38;
      var plotW = W - padL - padR, plotH = H - padT - padB;
      var nGroups = Math.max(labels.length, 1);
      var groupW = plotW / nGroups;
      var barW = Math.min(26, (groupW * 0.72) / datasets.length);
      var showValueOnBar = labels.length <= 6;

      var svg = '<svg viewBox="0 0 ' + W + ' ' + H + '" style="width:100%;height:214px;overflow:visible">';
      for (var g = 0; g <= 4; g++) {
        var gy = padT + plotH - (plotH * g / 4);
        var gVal = Math.round(maxVal * g / 4);
        svg += '<line x1="' + padL + '" y1="' + gy + '" x2="' + (W - padR) + '" y2="' + gy + '" stroke="#e2e8f0" stroke-dasharray="3,3"/>';
        svg += '<text x="' + (padL - 6) + '" y="' + (gy + 4) + '" text-anchor="end" font-size="10" fill="#647b92">' + gVal.toLocaleString() + '</text>';
      }
      labels.forEach(function(lbl, idx) {
        var gap = showValueOnBar ? 4 : 2;
        var totalBarsW = barW * datasets.length + (datasets.length - 1) * gap;
        var startX = padL + idx * groupW + (groupW - totalBarsW) / 2;
        datasets.forEach(function(ds, dIdx) {
          var val = ds.data[idx] || 0;
          var bh = Math.max(2, (val / maxVal) * plotH);
          var bx = startX + dIdx * (barW + gap);
          var by = padT + plotH - bh;
          svg += '<rect x="' + bx + '" y="' + by + '" width="' + barW + '" height="' + bh + '" rx="3" fill="' + ds.color + '"><title>' + lbl + ' - ' + ds.label + ': ' + val.toLocaleString() + '</title></rect>';
          if (showValueOnBar && val > 0) {
            svg += '<text x="' + (bx + barW / 2) + '" y="' + (by - 4) + '" text-anchor="middle" font-size="9.5" font-weight="700" fill="#244666">' + val.toLocaleString() + '</text>';
          }
        });
        var cx = padL + idx * groupW + groupW / 2;
        svg += '<text x="' + cx + '" y="' + (H - 11) + '" text-anchor="middle" font-size="11" font-weight="800" fill="#193653">' + lbl + '</text>';
      });
      svg += '</svg>';
      mountChartWithZoom(containerId, legendHtml + svg);
    }

    function renderSvgLineChart(containerId, labels, datasets) {
      var box = el(containerId);
      if (!box) return;
      var maxVal = 1;
      datasets.forEach(function(ds) {
        ds.data.forEach(function(v) { if (v > maxVal) maxVal = v; });
      });
      var legendHtml = '<div style="display:flex;gap:14px;justify-content:center;font-size:12px;margin-bottom:4px;flex-wrap:wrap">';
      datasets.forEach(function(ds) {
        legendHtml += '<span style="display:inline-flex;align-items:center;gap:5px"><i style="width:12px;height:4px;border-radius:2px;background:' + ds.color + ';display:inline-block"></i>' + ds.label + '</span>';
      });
      legendHtml += '</div>';

      var W = 560, H = 200, padL = 54, padR = 16, padT = 16, padB = 34;
      var plotW = W - padL - padR, plotH = H - padT - padB;
      var nPts = Math.max(labels.length - 1, 1);

      var svg = '<svg viewBox="0 0 ' + W + ' ' + H + '" style="width:100%;height:212px;overflow:visible">';
      for (var g = 0; g <= 4; g++) {
        var gy = padT + plotH - (plotH * g / 4);
        var gVal = Math.round(maxVal * g / 4);
        svg += '<line x1="' + padL + '" y1="' + gy + '" x2="' + (W - padR) + '" y2="' + gy + '" stroke="#e2e8f0" stroke-dasharray="3,3"/>';
        svg += '<text x="' + (padL - 6) + '" y="' + (gy + 4) + '" text-anchor="end" font-size="10" fill="#647b92">' + gVal.toLocaleString() + '</text>';
      }
      datasets.forEach(function(ds) {
        var pts = [];
        ds.data.forEach(function(val, idx) {
          var px = padL + (idx / nPts) * plotW;
          var py = padT + plotH - ((val || 0) / maxVal) * plotH;
          pts.push(px.toFixed(1) + "," + py.toFixed(1));
        });
        svg += '<polyline fill="none" stroke="' + ds.color + '" stroke-width="2.5" points="' + pts.join(" ") + '"/>';
        ds.data.forEach(function(val, idx) {
          var px = padL + (idx / nPts) * plotW;
          var py = padT + plotH - ((val || 0) / maxVal) * plotH;
          if (labels[idx] === selectedMonth || idx % 3 === 0 || idx === labels.length - 1) {
            var r = labels[idx] === selectedMonth ? 4.5 : 3;
            svg += '<circle cx="' + px.toFixed(1) + '" cy="' + py.toFixed(1) + '" r="' + r + '" fill="' + ds.color + '"><title>' + labels[idx] + ' ' + ds.label + ': ' + val.toLocaleString() + '</title></circle>';
          }
        });
      });
      labels.forEach(function(lbl, idx) {
        if (idx % 3 === 0 || idx === labels.length - 1) {
          var px = padL + (idx / nPts) * plotW;
          svg += '<text x="' + px.toFixed(1) + '" y="' + (H - 10) + '" text-anchor="middle" font-size="9.5" font-weight="700" fill="#47627d">' + lbl.slice(2) + '</text>';
        }
      });
      svg += '</svg>';
      mountChartWithZoom(containerId, legendHtml + svg);
    }

    // =========================================================================
    // 3B. 總處各區總和快覽 ＋ 表一/表二 5家拉BAR ＋ 業務餘額柱狀圖×成長率折線雙圖引擎
    // =========================================================================
    var BAR_WINDOW = 5;   // 分行窗格每次顯示 5 家分行
    var MONTH_WINDOW = 6; // 右側趨勢折線圖窗格每次顯示 6 個月份
    var sliderOffsetT1 = 0;
    var sliderOffsetT2 = 0;
    var compareSliderOffset = 0; // 業務項目深度比較區專屬分行拉 BAR 位移 (維持窗格內最多 5 家)
    var lineMonthOffset = 999;   // 右側趨勢折線圖專屬月份拉 BAR 位移 (維持窗格內最多 6 個月份)
    var cachedSortedBranches = [];
    var topBarChartScope = "BRANCH_5"; // "BRANCH_5" | "REGION_SUM" | "GROUP_SUM"

    var lineMetricKey = "dep"; // dep | loan | fund | rep | cls | weight | contrib
    var lineModeKey = "MOM";   // MOM | YOY | RAW
    var lineBranchSource = "SYNC_SLIDER"; // SYNC_SLIDER | REGIONS_ALL | GROUPS_ALL | CUSTOM
    var customPickedCodes = ["007", "005", "002", "004", "201"];

    var LINE_PALETTE = [
      "#2563eb", "#16a34a", "#d97706", "#dc2626",
      "#7c3aed", "#0891b2", "#db2777", "#4f46e5"
    ];

    var METRIC_META = {
      dep:     { name: "總存款餘額 (表一)", shortLabel: "存款餘額", unit: "萬", idx: 0, divisor: 1 },
      loan:    { name: "總授信餘額 (表一)", shortLabel: "授信餘額", unit: "萬", idx: 1, divisor: 1 },
      fund:    { name: "基金餘額 (表一)",   shortLabel: "基金餘額", unit: "萬", idx: 3, divisor: 1 },
      rep:     { name: "通報商機金額 (表二)", shortLabel: "通報金額", unit: "萬", idx: 10, divisor: 1 },
      cls:     { name: "實際成案金額 (表二)", shortLabel: "成案金額", unit: "萬", idx: 11, divisor: 1 },
      weight:  { name: "階段權重積分 (表二)", shortLabel: "權重積分", unit: "分", idx: 12, divisor: 10 },
      contrib: { name: "綜合總貢獻度 (雙表)", shortLabel: "綜合貢獻", unit: "點", idx: -1, divisor: 1 }
    };

    function syncAllMetricSelectors() {
      if (el("inlineBarMetricSelect")) el("inlineBarMetricSelect").value = lineMetricKey;
      if (el("inlineLineMetricSelect")) el("inlineLineMetricSelect").value = lineMetricKey;
      if (el("zoomMetricSelect")) el("zoomMetricSelect").value = lineMetricKey;
      if (el("lineModeSelect")) el("lineModeSelect").value = lineModeKey;
      if (el("zoomModeSelect")) el("zoomModeSelect").value = lineModeKey;
      var mPills = document.querySelectorAll("#lineMetricPills .metric-pill");
      for (var i = 0; i < mPills.length; i++) {
        mPills[i].classList.toggle("active", mPills[i].getAttribute("data-metric") === lineMetricKey);
      }
    }

    function getBranchMetricValue(bObj, ym, mKey) {
      if (!bObj || !ym || !bObj.m[ym]) return 0;
      var arr = bObj.m[ym];
      if (mKey === "contrib") return arr[5] + arr[14];
      var info = METRIC_META[mKey] || METRIC_META.dep;
      return arr[info.idx] / info.divisor;
    }

    function formatMetricVal(val, mKey) {
      if (mKey === "weight") return val.toFixed(1) + " 分";
      if (mKey === "contrib") return Math.round(val).toLocaleString("en-US") + " 點";
      return formatWanToReadable(val);
    }

    var hqRegMetricKey = "dep";
    var hqRegModeKey = "MOM";
    var hqRegMonthOffset = 999;

    // 建立「全行 4 大業務分區（北區／桃竹苗區／中區／南區）總和」或「5大組別總和」的彙總虛擬單位物件 (含 23 個月完整 m[ym] 陣列)
    function buildAggregatedUnitObjects(mode) {
      var names = mode === "REGIONS"
        ? ["北區", "桃竹苗區", "中區", "南區"]
        : ["第一組", "第二組", "第三組", "第四組", "第五組"];

      return names.map(function(nm) {
        var sub = branchMonthlyList.filter(function(b) {
          if (currentRole === "REGION" && b.region !== lockedRegion) return false;
          if (currentRole === "BRANCH" && b.code !== lockedBranch) return false;
          return mode === "REGIONS" ? (b.region === nm) : (b.group === nm);
        });
        var mMap = {};
        allMonths.forEach(function(ym) {
          var sumArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
          sub.forEach(function(b) {
            var bm = b.m[ym];
            if (bm) {
              for (var k = 0; k < 15; k++) sumArr[k] += bm[k];
            }
          });
          mMap[ym] = sumArr;
        });
        var cCnt = 0, gCnt = 0;
        sub.forEach(function(b) { cCnt += b.custCount; gCnt += b.gebCount; });
        return {
          isAggUnit: true,
          aggType: mode,
          code: nm,
          name: "總和 (" + sub.length + "家)",
          region: mode === "REGIONS" ? nm : "跨區組別",
          subRegion: "共 " + sub.length + " 家分行",
          group: mode === "GROUPS" ? nm : ("轄下 " + cCnt + " 戶"),
          custCount: cCnt,
          gebCount: gCnt,
          branchCount: sub.length,
          m: mMap
        };
      }).filter(function(u) { return u.branchCount > 0; });
    }

    // 總處專用：渲染「全行 4 大業務分區（北區／桃竹苗區／中區／南區）發展狀況圖表組」
    function renderHqRegionsDevelopmentCharts(regUnits) {
      if (!regUnits || !regUnits.length) return;

      if (el("hqRegBarMetricSelect")) el("hqRegBarMetricSelect").value = hqRegMetricKey;
      if (el("hqRegLineMetricSelect")) el("hqRegLineMetricSelect").value = hqRegMetricKey;
      if (el("hqRegModeSelect")) el("hqRegModeSelect").value = hqRegModeKey;

      var rLabels = regUnits.map(function(u) { return u.code + "(" + u.branchCount + "家)"; });
      renderSvgBarChart("chartHqRegT1", rLabels, [
        { label: "總存款(百萬)", data: regUnits.map(function(u) { return Math.round(u.m[selectedMonth][0] / 100); }), color: "#2878e5" },
        { label: "總授信(百萬)", data: regUnits.map(function(u) { return Math.round(u.m[selectedMonth][1] / 100); }), color: "#20a55a" },
        { label: "基金總額(百萬)", data: regUnits.map(function(u) { return Math.round(u.m[selectedMonth][3] / 100); }), color: "#f1b638" }
      ]);

      renderSvgBarChart("chartHqRegT2", rLabels, [
        { label: "當月通報總額(百萬)", data: regUnits.map(function(u) { return Math.round(u.m[selectedMonth][10] / 100); }), color: "#3b82f6" },
        { label: "當月成案總額(百萬)", data: regUnits.map(function(u) { return Math.round(u.m[selectedMonth][11] / 100); }), color: "#16834a" }
      ]);

      var mInfo = METRIC_META[hqRegMetricKey] || METRIC_META.dep;
      // 渲染 4 大分區之三期餘額柱狀圖 (#chartHqRegBar)
      renderComboBalanceBarAndGrowthChart(regUnits, mInfo, "chartHqRegBar", "hqRegBarTitle", null, hqRegMetricKey);

      // 渲染 4 大分區之 6 個月逐月趨勢折線＋各月餘額柱狀圖 (#chartHqRegLine)
      var availMonths = (hqRegModeKey === "MOM")
        ? allMonths.slice(1)
        : (hqRegModeKey === "YOY" ? allMonths.filter(function(ym) { return getYoYMonth(ym) !== null; }) : allMonths.slice());
      var maxMOff = Math.max(0, availMonths.length - MONTH_WINDOW);
      if (hqRegMonthOffset > maxMOff) hqRegMonthOffset = maxMOff;
      if (hqRegMonthOffset < 0) hqRegMonthOffset = 0;
      var cMonths = availMonths.slice(hqRegMonthOffset, hqRegMonthOffset + MONTH_WINDOW);

      var hqSlider = el("sliderHqRegMonths");
      var hqRangeTxt = el("hqRegMonthRangeText");
      if (hqSlider && hqRangeTxt) {
        hqSlider.max = String(maxMOff);
        hqSlider.value = String(hqRegMonthOffset);
        hqSlider.disabled = availMonths.length <= MONTH_WINDOW;
        hqRangeTxt.textContent = cMonths.length ? (cMonths[0] + " ～ " + cMonths[cMonths.length - 1] + " (6個月)") : "";
      }

      var rawDiv = (mInfo.unit === "萬") ? 100 : 1;
      var dispUnit = (rawDiv === 100) ? "百萬" : mInfo.unit;
      var modeTitle = hqRegModeKey === "MOM" ? "月增減率 MoM (%)" : (hqRegModeKey === "YOY" ? "年增減率 YoY (%)" : ("實際數值 (" + dispUnit + ")"));
      if (el("hqRegLineUnitBadge")) {
        el("hqRegLineUnitBadge").textContent = "左軸：" + modeTitle + " ｜ 右軸：" + mInfo.shortLabel + "(" + dispUnit + ")";
      }

      var datasets = regUnits.map(function(b, bIdx) {
        var color = LINE_PALETTE[bIdx % LINE_PALETTE.length];
        var rawSeries = [];
        var series = cMonths.map(function(ym) {
          var curVal = getBranchMetricValue(b, ym, hqRegMetricKey);
          rawSeries.push(Number((curVal / rawDiv).toFixed(1)));
          if (hqRegModeKey === "MOM") {
            var prevYm = getPrevMonth(ym);
            var prevVal = prevYm ? getBranchMetricValue(b, prevYm, hqRegMetricKey) : 0;
            return (!prevVal || prevVal <= 0) ? 0 : Number((((curVal - prevVal) / prevVal) * 100).toFixed(1));
          } else if (hqRegModeKey === "YOY") {
            var yoyYm = getYoYMonth(ym);
            var yoyVal = yoyYm ? getBranchMetricValue(b, yoyYm, hqRegMetricKey) : 0;
            return (!yoyVal || yoyVal <= 0) ? 0 : Number((((curVal - yoyVal) / yoyVal) * 100).toFixed(1));
          }
          return Number((curVal / rawDiv).toFixed(1));
        });
        return { branch: b, label: b.code + "總和", color: color, data: series, rawBars: rawSeries };
      });

      var minVal = Infinity, maxVal = -Infinity, maxRawBar = 1;
      datasets.forEach(function(ds) {
        ds.data.forEach(function(v) { if (v < minVal) minVal = v; if (v > maxVal) maxVal = v; });
        ds.rawBars.forEach(function(rv) { if (rv > maxRawBar) maxRawBar = rv; });
      });
      var isPct = (hqRegModeKey === "MOM" || hqRegModeKey === "YOY");
      if (isPct) {
        if (minVal > -2) minVal = -2;
        if (maxVal < 5) maxVal = 5;
        var padR = (maxVal - minVal) * 0.14;
        minVal = Math.floor(minVal - padR);
        maxVal = Math.ceil(maxVal + padR);
      } else {
        minVal = 0;
        maxVal = Math.max(Math.ceil(maxVal * 1.15), 10);
      }
      var valSpan = Math.max(maxVal - minVal, 1);
      var maxBarAxis = Math.max(Math.ceil(maxRawBar * 1.25), 4);

      var legendHtml = '<div style="display:flex;gap:12px;justify-content:center;font-size:11.5px;margin-bottom:4px;flex-wrap:wrap;font-weight:700">';
      datasets.forEach(function(ds) {
        legendHtml += '<span style="display:inline-flex;align-items:center;gap:5px"><i style="width:14px;height:4px;border-radius:2px;background:' + ds.color + ';display:inline-block"></i><span style="color:#193653">' + ds.label + '</span></span>';
      });
      legendHtml += '</div>';

      var W = 640, H = 224, padL = 56, padRight = 112, padT = 24, padB = 36;
      var plotW = W - padL - padRight, plotH = H - padT - padB;
      var nCols = Math.max(cMonths.length, 1);
      var colW = plotW / nCols;
      function mToX(i) { return padL + i * colW + colW / 2; }
      function vToY(v) { return padT + plotH - ((v - minVal) / valSpan) * plotH; }

      var svg = '<svg viewBox="0 0 ' + W + ' ' + H + '" style="width:100%;height:228px;overflow:visible">';
      svg += '<text x="' + (padL - 6) + '" y="12" text-anchor="start" font-size="9.5" font-weight="800" fill="#47627d">◀ 左軸：' + modeTitle + '</text>';
      svg += '<text x="' + (W - padRight + 6) + '" y="12" text-anchor="start" font-size="9.5" font-weight="800" fill="#1d4ed8">右軸：' + mInfo.shortLabel + ' (' + dispUnit + ') ▶</text>';

      for (var g = 0; g <= 4; g++) {
        var gVal = minVal + (valSpan * g / 4);
        var gy = padT + plotH - (plotH * g / 4);
        var rBarVal = Math.round(maxBarAxis * g / 4);
        var lblStr = isPct ? (gVal > 0 ? "+" + gVal.toFixed(1) + "%" : gVal.toFixed(1) + "%") : Math.round(gVal).toLocaleString();
        svg += '<line x1="' + padL + '" y1="' + gy.toFixed(1) + '" x2="' + (W - padRight) + '" y2="' + gy.toFixed(1) + '" stroke="#e2e8f0" stroke-dasharray="3,3"/>';
        svg += '<text x="' + (padL - 6) + '" y="' + (gy + 4).toFixed(1) + '" text-anchor="end" font-size="9.5" font-weight="700" fill="#647b92">' + lblStr + '</text>';
        svg += '<text x="' + (W - padRight + 6) + '" y="' + (gy + 4).toFixed(1) + '" text-anchor="start" font-size="9.5" font-weight="800" fill="#1d4ed8">' + mInfo.shortLabel + ' ' + rBarVal.toLocaleString() + dispUnit + '</text>';
      }

      var subBarW = Math.max(5, Math.min(12, (colW * 0.68) / datasets.length));
      cMonths.forEach(function(ym, mIdx) {
        var cx = mToX(mIdx);
        var startBx = cx - (subBarW * datasets.length) / 2;
        datasets.forEach(function(ds, dIdx) {
          var rv = ds.rawBars[mIdx] || 0;
          var bh = Math.max(2, (rv / maxBarAxis) * plotH);
          var bx = startBx + dIdx * subBarW;
          var by = padT + plotH - bh;
          svg += '<rect x="' + bx.toFixed(1) + '" y="' + by.toFixed(1) + '" width="' + (subBarW - 1).toFixed(1) + '" height="' + bh.toFixed(1) + '" rx="2" fill="' + ds.color + '" opacity="0.28"><title>[' + ym + '] ' + ds.label + '｜' + mInfo.shortLabel + '：' + rv.toLocaleString() + ' ' + dispUnit + '</title></rect>';
        });
      });

      if (isPct && minVal <= 0 && maxVal >= 0) {
        var zeroY = vToY(0);
        svg += '<line x1="' + padL + '" y1="' + zeroY.toFixed(1) + '" x2="' + (W - padRight) + '" y2="' + zeroY.toFixed(1) + '" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,3"/>';
        svg += '<text x="' + (padL + 4) + '" y="' + (zeroY - 4).toFixed(1) + '" font-size="9" font-weight="800" fill="#dc2626">0% 基準線</text>';
      }

      datasets.forEach(function(ds) {
        var pts = ds.data.map(function(v, idx) { return mToX(idx).toFixed(1) + "," + vToY(v).toFixed(1); });
        svg += '<polyline fill="none" stroke="' + ds.color + '" stroke-width="2.5" points="' + pts.join(" ") + '"/>';
        ds.data.forEach(function(v, idx) {
          var px = mToX(idx), py = vToY(v);
          var isCurM = cMonths[idx] === selectedMonth;
          var vStr = isPct ? ((v >= 0 ? "+" : "") + v.toFixed(1) + "%") : (v.toLocaleString() + " " + dispUnit);
          svg += '<circle cx="' + px.toFixed(1) + '" cy="' + py.toFixed(1) + '" r="' + (isCurM ? 4.8 : 3.6) + '" fill="' + ds.color + '" stroke="#fff" stroke-width="1.2"><title>[' + cMonths[idx] + '] ' + ds.label + '｜' + mInfo.shortLabel + ': ' + ds.rawBars[idx].toLocaleString() + ' ' + dispUnit + '｜' + modeTitle + ': ' + vStr + '</title></circle>';
          if (isCurM || idx === cMonths.length - 1) {
            svg += '<text x="' + px.toFixed(1) + '" y="' + (py - 7).toFixed(1) + '" text-anchor="middle" font-size="9.5" font-weight="800" fill="' + ds.color + '">' + vStr + '</text>';
          }
        });
      });

      cMonths.forEach(function(ym, idx) {
        var px = mToX(idx);
        var isSel = ym === selectedMonth;
        svg += '<text x="' + px.toFixed(1) + '" y="' + (H - 10) + '" text-anchor="middle" font-size="' + (isSel ? "11" : "10.5") + '" font-weight="' + (isSel ? "900" : "700") + '" fill="' + (isSel ? "#082d5b" : "#334155") + '">' + ym + '</text>';
      });
      svg += '</svg>';
      mountChartWithZoom("chartHqRegLine", legendHtml + svg);
    }

    // 總處專用：在主畫面直接渲染「全行 4 大業務分區（北區／桃竹苗區／中區／南區）總和一覽卡與發展狀況圖表」
    function renderHqRegionTotalsStrip() {
      var sec = el("hqRegionTotalsSection");
      if (!sec) return;
      if (currentRole !== "HQ") {
        sec.style.display = "none";
        return;
      }
      sec.style.display = "block";
      var activeRegFilter = el("warRegionFilter").value;
      el("btnResetAllRegions").style.display = activeRegFilter !== "ALL" ? "inline-block" : "none";

      var momYm = getPrevMonth(selectedMonth);
      var yoyYm = getYoYMonth(selectedMonth);
      var regUnits = buildAggregatedUnitObjects("REGIONS");
      var grid = el("hqRegionTotalsGrid");
      grid.innerHTML = "";

      regUnits.forEach(function(ru) {
        var cur = ru.m[selectedMonth];
        var mom = momYm ? ru.m[momYm] : null;
        var yoy = yoyYm ? ru.m[yoyYm] : null;

        var card = document.createElement("div");
        card.className = "region-sum-card" + (activeRegFilter === ru.code ? " active" : "");
        card.innerHTML =
          '<div class="region-sum-head">' +
            '<span>🗺️ ' + ru.code + '總和</span>' +
            '<span class="demo" style="font-size:11px;padding:1px 7px">' + ru.branchCount + '家分行 / ' + ru.custCount + '戶</span>' +
          '</div>' +
          '<div class="region-sum-row"><span>💰 存款總和：</span><b>' + formatWanToReadable(cur[0]) + '</b></div>' +
          '<div class="delta-row" style="margin-bottom:4px">' + deltaBadgeHtml("MoM", cur[0], mom ? mom[0] : 0) + deltaBadgeHtml("YoY", cur[0], yoy ? yoy[0] : 0) + '</div>' +
          '<div class="region-sum-row"><span>🤝 授信總和：</span><b>' + formatWanToReadable(cur[1]) + '</b></div>' +
          '<div class="delta-row" style="margin-bottom:4px">' + deltaBadgeHtml("MoM", cur[1], mom ? mom[1] : 0) + deltaBadgeHtml("YoY", cur[1], yoy ? yoy[1] : 0) + '</div>' +
          '<div class="region-sum-row"><span>📈 基金總和：</span><b>' + formatWanToReadable(cur[3]) + '</b></div>' +
          '<div class="region-sum-row"><span>📢 通報商機：</span><b>' + formatWanToReadable(cur[10]) + '</b></div>' +
          '<div class="region-sum-row"><span>✅ 實際成案：</span><b style="color:var(--green)">' + formatWanToReadable(cur[11]) + '</b></div>' +
          '<div class="delta-row">' + deltaBadgeHtml("成案MoM", cur[11], mom ? mom[11] : 0) + deltaBadgeHtml("YoY", cur[11], yoy ? yoy[11] : 0) + '</div>';

        card.addEventListener("click", function() {
          if (el("warRegionFilter").value === ru.code) {
            el("warRegionFilter").value = "ALL";
            toast("🔄 已恢復檢視【全行 4 大業務分區】");
          } else {
            el("warRegionFilter").value = ru.code;
            toast("🗺️ 已篩選檢視【" + ru.code + "】轄下 " + ru.branchCount + " 家分行與總和");
          }
          sliderOffsetT1 = 0;
          sliderOffsetT2 = 0;
          drawWarRoom();
        });
        grid.appendChild(card);
      });

      // 同步渲染總處「全行 4 大業務分區發展狀況圖表組」
      renderHqRegionsDevelopmentCharts(regUnits);
    }

    // 渲染表一與表二柱狀圖 (支援：5家分行拉BAR / 5大業務分區總和 / 5大組別總和)
    function render5BranchBarCharts() {
      var scopePills = document.querySelectorAll("#topBarChartScopePills .metric-pill");
      for (var sp = 0; sp < scopePills.length; sp++) {
        scopePills[sp].classList.toggle("active", scopePills[sp].getAttribute("data-bscope") === topBarChartScope);
      }

      var isBranchMode = (topBarChartScope === "BRANCH_5");
      el("sliderWrapT1").style.display = isBranchMode ? "flex" : "none";
      el("sliderWrapT2").style.display = isBranchMode ? "flex" : "none";

      if (topBarChartScope === "REGION_SUM") {
        var rUnits = buildAggregatedUnitObjects("REGIONS");
        var rLabels = rUnits.map(function(u) { return u.code + "(" + u.branchCount + "家)"; });
        el("sliderT1RangeText").textContent = "目前顯示：全行 4 大業務分區總和";
        el("chart1Title").textContent = "🗺️ 表一：全行 4 大業務分區「存款／授信／基金總和」對比（單位：百萬）";
        renderSvgBarChart("chartBranchBalances", rLabels, [
          { label: "總存款(百萬)", data: rUnits.map(function(u) { return Math.round(u.m[selectedMonth][0] / 100); }), color: "#2878e5" },
          { label: "總授信(百萬)", data: rUnits.map(function(u) { return Math.round(u.m[selectedMonth][1] / 100); }), color: "#20a55a" },
          { label: "基金總額(百萬)", data: rUnits.map(function(u) { return Math.round(u.m[selectedMonth][3] / 100); }), color: "#f1b638" }
        ]);

        el("sliderT2RangeText").textContent = "目前顯示：全行 4 大業務分區總和";
        el("chart2Title").textContent = "🗺️ 表二：全行 4 大業務分區「通報商機 vs 實際成案總和」對比（單位：百萬）";
        renderSvgBarChart("chartBranchConversion", rLabels, [
          { label: "當月通報總額(百萬)", data: rUnits.map(function(u) { return Math.round(u.m[selectedMonth][10] / 100); }), color: "#3b82f6" },
          { label: "當月成案總額(百萬)", data: rUnits.map(function(u) { return Math.round(u.m[selectedMonth][11] / 100); }), color: "#16834a" }
        ]);
        return;
      }

      if (topBarChartScope === "GROUP_SUM") {
        var gUnits = buildAggregatedUnitObjects("GROUPS");
        var gLabels = gUnits.map(function(u) { return u.code + "(" + u.branchCount + "家)"; });
        el("sliderT1RangeText").textContent = "目前顯示：5 大規模組別總和";
        el("chart1Title").textContent = "🏢 表一：各規模組別「存款／授信／基金總和」對比（單位：百萬）";
        renderSvgBarChart("chartBranchBalances", gLabels, [
          { label: "總存款(百萬)", data: gUnits.map(function(u) { return Math.round(u.m[selectedMonth][0] / 100); }), color: "#2878e5" },
          { label: "總授信(百萬)", data: gUnits.map(function(u) { return Math.round(u.m[selectedMonth][1] / 100); }), color: "#20a55a" },
          { label: "基金總額(百萬)", data: gUnits.map(function(u) { return Math.round(u.m[selectedMonth][3] / 100); }), color: "#f1b638" }
        ]);

        el("sliderT2RangeText").textContent = "目前顯示：5 大規模組別總和";
        el("chart2Title").textContent = "🏢 表二：各規模組別「通報商機 vs 實際成案總和」對比（單位：百萬）";
        renderSvgBarChart("chartBranchConversion", gLabels, [
          { label: "當月通報總額(百萬)", data: gUnits.map(function(u) { return Math.round(u.m[selectedMonth][10] / 100); }), color: "#3b82f6" },
          { label: "當月成案總額(百萬)", data: gUnits.map(function(u) { return Math.round(u.m[selectedMonth][11] / 100); }), color: "#16834a" }
        ]);
        return;
      }

      var total = cachedSortedBranches.length;
      var maxOffset = Math.max(0, total - BAR_WINDOW);

      if (sliderOffsetT1 > maxOffset) sliderOffsetT1 = maxOffset;
      if (sliderOffsetT1 < 0) sliderOffsetT1 = 0;
      if (sliderOffsetT2 > maxOffset) sliderOffsetT2 = maxOffset;
      if (sliderOffsetT2 < 0) sliderOffsetT2 = 0;

      var s1 = el("sliderT1");
      var s2 = el("sliderT2");
      if (s1) {
        s1.max = String(maxOffset);
        s1.value = String(sliderOffsetT1);
        s1.disabled = total <= BAR_WINDOW;
      }
      if (s2) {
        s2.max = String(maxOffset);
        s2.value = String(sliderOffsetT2);
        s2.disabled = total <= BAR_WINDOW;
      }

      // 表一 5 家分行切片
      var slice1 = cachedSortedBranches.slice(sliderOffsetT1, sliderOffsetT1 + BAR_WINDOW);
      var start1 = total > 0 ? (sliderOffsetT1 + 1) : 0;
      var end1 = Math.min(sliderOffsetT1 + BAR_WINDOW, total);
      el("sliderT1RangeText").textContent = "目前顯示：第 " + start1 + " ～ " + end1 + " 名 / 共 " + total + " 家分行";
      el("chart1Title").textContent = "🏦 表一：各分行「存款／授信／基金餘額」對比（第 " + start1 + "~" + end1 + " 名，單位：萬）";

      var labels1 = slice1.map(function(b, idx) {
        return "#" + (sliderOffsetT1 + idx + 1) + " " + b.code + b.name.replace("分行", "");
      });
      renderSvgBarChart("chartBranchBalances", labels1, [
        { label: "總存款(萬)", data: slice1.map(function(b) { return b.m[selectedMonth][0]; }), color: "#2878e5" },
        { label: "總授信(萬)", data: slice1.map(function(b) { return b.m[selectedMonth][1]; }), color: "#20a55a" },
        { label: "基金餘額(萬)", data: slice1.map(function(b) { return b.m[selectedMonth][3]; }), color: "#f1b638" }
      ]);

      // 表二 5 家分行切片
      var slice2 = cachedSortedBranches.slice(sliderOffsetT2, sliderOffsetT2 + BAR_WINDOW);
      var start2 = total > 0 ? (sliderOffsetT2 + 1) : 0;
      var end2 = Math.min(sliderOffsetT2 + BAR_WINDOW, total);
      el("sliderT2RangeText").textContent = "目前顯示：第 " + start2 + " ～ " + end2 + " 名 / 共 " + total + " 家分行";
      el("chart2Title").textContent = "🚀 表二：各分行「通報商機 vs 實際成案金額」對比（第 " + start2 + "~" + end2 + " 名，單位：萬）";

      var labels2 = slice2.map(function(b, idx) {
        return "#" + (sliderOffsetT2 + idx + 1) + " " + b.code + b.name.replace("分行", "");
      });
      renderSvgBarChart("chartBranchConversion", labels2, [
        { label: "當月通報金額(萬)", data: slice2.map(function(b) { return b.m[selectedMonth][10]; }), color: "#3b82f6" },
        { label: "當月成案金額(萬)", data: slice2.map(function(b) { return b.m[selectedMonth][11]; }), color: "#16834a" }
      ]);

      // 若多分行比較圖設為同步拉 BAR，則連動更新
      if (lineBranchSource === "SYNC_SLIDER") {
        renderMultiBranchCompareSection();
      }
    }

    function stepSlider(which, delta) {
      var total = cachedSortedBranches.length;
      var maxOffset = Math.max(0, total - BAR_WINDOW);
      var isSync = el("syncSlidersChk") && el("syncSlidersChk").checked;

      if (which === 1 || isSync) {
        sliderOffsetT1 = Math.max(0, Math.min(maxOffset, sliderOffsetT1 + delta));
      }
      if (which === 2 || isSync) {
        sliderOffsetT2 = isSync ? sliderOffsetT1 : Math.max(0, Math.min(maxOffset, sliderOffsetT2 + delta));
      }
      render5BranchBarCharts();
    }

    function renderCustomBranchChips() {
      var container = el("customBranchChipContainer");
      if (!container) return;
      var q = (el("customBranchSearchInput").value || "").trim().toLowerCase();
      container.innerHTML = "";

      cachedSortedBranches.forEach(function(b, rankIdx) {
        if (q && b.code.toLowerCase().indexOf(q) === -1 && b.name.toLowerCase().indexOf(q) === -1 && b.region.toLowerCase().indexOf(q) === -1) {
          return;
        }
        var isPicked = customPickedCodes.indexOf(b.code) !== -1;
        var span = document.createElement("span");
        span.className = "branch-chip" + (isPicked ? " on" : "");
        span.innerHTML = (isPicked ? "☑️ " : "⬜ ") + "#" + (rankIdx + 1) + " " + b.code + " " + b.name.replace("分行", "") + " <small style='color:#647b92'>(" + b.region + ")</small>";
        span.addEventListener("click", function() {
          var pos = customPickedCodes.indexOf(b.code);
          if (pos !== -1) {
            if (customPickedCodes.length <= 1) {
              toast("⚠️ 請至少保留 1 家分行進行比較");
              return;
            }
            customPickedCodes.splice(pos, 1);
          } else {
            customPickedCodes.push(b.code);
            // 當新勾選的分行超過 5 家時，自動將下方拉 BAR 移至包含最新勾選分行的窗格位置，維持窗格內只有 5 家
            var pickedListNow = cachedSortedBranches.filter(function(x) {
              return customPickedCodes.indexOf(x.code) !== -1;
            });
            var newIdx = -1;
            for (var pi = 0; pi < pickedListNow.length; pi++) {
              if (pickedListNow[pi].code === b.code) { newIdx = pi; break; }
            }
            if (pickedListNow.length > BAR_WINDOW && newIdx !== -1) {
              if (newIdx >= compareSliderOffset + BAR_WINDOW) {
                compareSliderOffset = newIdx - BAR_WINDOW + 1;
              } else if (newIdx < compareSliderOffset) {
                compareSliderOffset = newIdx;
              }
            }
          }
          renderCustomBranchChips();
          renderMultiBranchCompareSection();
        });
        container.appendChild(span);
      });
    }

    // 左圖渲染器：繪製【對應業務項目之餘額／實績分組柱狀圖 (去年同月 / 上月 / 當月)】（移除跨分行折線，維持純粹各單位三期餘額柱狀對比）
    function renderComboBalanceBarAndGrowthChart(targetUnits, mInfo, customBoxId, customTitleId, customBadgeId, customMetricKey) {
      var boxId = customBoxId || "chartMultiBranchBar";
      var titleId = customTitleId || "comboBarChartTitle";
      var badgeId = customBadgeId || "comboBarUnitBadge";
      var metricKey = customMetricKey || lineMetricKey;
      var box = el(boxId);
      if (!box) return;
      if (!targetUnits.length) {
        box.innerHTML = '<div style="text-align:center;padding-top:90px;color:#647b92">無比較單位資料</div>';
        return;
      }

      var momYm = getPrevMonth(selectedMonth);
      var yoyYm = getYoYMonth(selectedMonth);
      var isLargeRegion = targetUnits[0] && targetUnits[0].isAggUnit;
      var scaleDiv = (isLargeRegion && mInfo.unit === "萬") ? 100 : 1; // 分區總和若為「萬」自動轉為「百萬」顯示更精煉
      var dispUnit = (scaleDiv === 100) ? "百萬" : mInfo.unit;

      if (el(titleId)) el(titleId).textContent = "餘額／實績柱狀圖（去年同月／上月／當月對比）";
      if (el(badgeId)) el(badgeId).textContent = "單位：" + dispUnit + (boxId === "chartHqRegBar" ? "（全行 4 大分區對比）" : "（窗格維持 5 家）");

      var unitItems = targetUnits.map(function(u, idx) {
        var curRaw = getBranchMetricValue(u, selectedMonth, metricKey);
        var momRaw = momYm ? getBranchMetricValue(u, momYm, metricKey) : 0;
        var yoyRaw = yoyYm ? getBranchMetricValue(u, yoyYm, metricKey) : 0;

        var momPct = (momRaw > 0) ? Number((((curRaw - momRaw) / momRaw) * 100).toFixed(1)) : 0;
        var yoyPct = (yoyRaw > 0) ? Number((((curRaw - yoyRaw) / yoyRaw) * 100).toFixed(1)) : 0;

        return {
          u: u,
          shortLabel: u.isAggUnit ? u.code : (u.code + u.name.replace("分行", "")),
          color: LINE_PALETTE[idx % LINE_PALETTE.length],
          yoyVal: Number((yoyRaw / scaleDiv).toFixed(1)),
          momVal: Number((momRaw / scaleDiv).toFixed(1)),
          curVal: Number((curRaw / scaleDiv).toFixed(1)),
          curRaw: curRaw,
          momPct: momPct,
          yoyPct: yoyPct
        };
      });

      var maxBar = 1;
      unitItems.forEach(function(it) {
        if (it.yoyVal > maxBar) maxBar = it.yoyVal;
        if (it.momVal > maxBar) maxBar = it.momVal;
        if (it.curVal > maxBar) maxBar = it.curVal;
      });
      maxBar = Math.ceil(maxBar * 1.18);

      var legendHtml =
        '<div style="display:flex;gap:14px;justify-content:center;font-size:11.5px;margin-bottom:4px;flex-wrap:wrap;font-weight:700">' +
          '<span style="display:inline-flex;align-items:center;gap:5px"><i style="width:11px;height:11px;border-radius:2px;background:#cbd5e1;display:inline-block"></i>去年同月 (' + (yoyYm || "無") + ') 餘額</span>' +
          '<span style="display:inline-flex;align-items:center;gap:5px"><i style="width:11px;height:11px;border-radius:2px;background:#93c5fd;display:inline-block"></i>上月 (' + (momYm || "無") + ') 餘額</span>' +
          '<span style="display:inline-flex;align-items:center;gap:5px"><i style="width:11px;height:11px;border-radius:2px;background:#2563eb;display:inline-block"></i>當月 (' + selectedMonth + ') 餘額</span>' +
        '</div>';

      var W = 620, H = 228, padL = 56, padR = 108, padT = 24, padB = 38;
      var plotW = W - padL - padR, plotH = H - padT - padB;
      var nGroups = Math.max(unitItems.length, 1);
      var groupW = plotW / nGroups;
      var barW = Math.min(22, (groupW * 0.72) / 3);

      var svg = '<svg viewBox="0 0 ' + W + ' ' + H + '" style="width:100%;height:236px;overflow:visible">';

      // 水平格線與左右軸餘額刻度（右側同步標示「存款餘額 XXX萬」等業務類別對應單位座標）
      for (var g = 0; g <= 4; g++) {
        var gy = padT + plotH - (plotH * g / 4);
        var bVal = Math.round(maxBar * g / 4);
        svg += '<line x1="' + padL + '" y1="' + gy.toFixed(1) + '" x2="' + (W - padR) + '" y2="' + gy.toFixed(1) + '" stroke="#e2e8f0" stroke-dasharray="3,3"/>';
        svg += '<text x="' + (padL - 6) + '" y="' + (gy + 4).toFixed(1) + '" text-anchor="end" font-size="9.5" font-weight="700" fill="#47627d">' + bVal.toLocaleString() + '</text>';
        svg += '<text x="' + (W - padR + 6) + '" y="' + (gy + 4).toFixed(1) + '" text-anchor="start" font-size="9.5" font-weight="800" fill="#1d4ed8">' + mInfo.shortLabel + ' ' + bVal.toLocaleString() + dispUnit + '</text>';
      }

      // 分組餘額柱狀圖 (去年同月 / 上月 / 當月) — 統一三期色塊：灰 (#cbd5e1)、淺藍 (#93c5fd)、深藍 (#2563eb)
      unitItems.forEach(function(it, idx) {
        var totalW = barW * 3 + 6;
        var sx = padL + idx * groupW + (groupW - totalW) / 2;
        var bars = [
          { lbl: "去年同月(" + (yoyYm || "無") + ")", v: it.yoyVal, c: "#cbd5e1" },
          { lbl: "上月(" + (momYm || "無") + ")",     v: it.momVal, c: "#93c5fd" },
          { lbl: "當月(" + selectedMonth + ")",       v: it.curVal, c: "#2563eb" }
        ];
        bars.forEach(function(bItem, bIdx) {
          var bh = Math.max(2, (bItem.v / maxBar) * plotH);
          var bx = sx + bIdx * (barW + 3);
          var by = padT + plotH - bh;
          var tipText = it.shortLabel + "｜" + bItem.lbl + " " + mInfo.name + "：" + bItem.v.toLocaleString() + " " + dispUnit +
                        "（月增減 MoM: " + (it.momPct >= 0 ? "+" : "") + it.momPct + "% / 年增減 YoY: " + (it.yoyPct >= 0 ? "+" : "") + it.yoyPct + "%）";
          svg += '<rect x="' + bx.toFixed(1) + '" y="' + by.toFixed(1) + '" width="' + barW.toFixed(1) + '" height="' + bh.toFixed(1) + '" rx="3" fill="' + bItem.c + '" opacity="' + (bIdx === 2 ? "0.96" : "0.85") + '"><title>' + tipText + '</title></rect>';
          if (bIdx === 2) {
            // 在當月餘額柱頂統一以深藍色標示金額
            svg += '<text x="' + (bx + barW / 2).toFixed(1) + '" y="' + (by - 5).toFixed(1) + '" text-anchor="middle" font-size="10" font-weight="800" fill="#1d4ed8">' + bItem.v.toLocaleString() + '</text>';
          }
        });

        var cx = padL + idx * groupW + groupW / 2;
        svg += '<text x="' + cx.toFixed(1) + '" y="' + (H - 12) + '" text-anchor="middle" font-size="10.5" font-weight="800" fill="#193653">' + it.shortLabel + '</text>';
      });

      svg += '</svg>';
      mountChartWithZoom(boxId, legendHtml + svg);
    }

    function stepCompareSlider(delta) {
      var allList = cachedSortedBranches.filter(function(b) {
        return customPickedCodes.indexOf(b.code) !== -1;
      });
      var maxOff = Math.max(0, allList.length - BAR_WINDOW);
      compareSliderOffset = Math.max(0, Math.min(maxOff, compareSliderOffset + delta));
      renderMultiBranchCompareSection();
    }

    function getAvailableTimelineMonths() {
      if (lineModeKey === "MOM") {
        return allMonths.slice(1);
      } else if (lineModeKey === "YOY") {
        return allMonths.filter(function(ym) { return getYoYMonth(ym) !== null; });
      }
      return allMonths.slice();
    }

    function stepLineMonthSlider(delta) {
      var avail = getAvailableTimelineMonths();
      var maxOff = Math.max(0, avail.length - MONTH_WINDOW);
      lineMonthOffset = Math.max(0, Math.min(maxOff, lineMonthOffset + delta));
      renderMultiBranchCompareSection();
    }

    // 渲染業務項目比較專區 (同時渲染：左圖「餘額柱狀圖 (5家窗格+拉BAR)」 與 右圖「逐月成長率折線＋背景各月餘額柱狀圖 (6個月窗格+拉BAR)」 與 下方明細表)
    function renderMultiBranchCompareSection() {
      var box = el("chartMultiBranchLine");
      if (!box) return;

      syncAllMetricSelectors();
      var mInfo = METRIC_META[lineMetricKey] || METRIC_META.dep;
      var allTargetBranches = [];

      if (lineBranchSource === "REGIONS_ALL") {
        allTargetBranches = buildAggregatedUnitObjects("REGIONS");
      } else if (lineBranchSource === "GROUPS_ALL") {
        allTargetBranches = buildAggregatedUnitObjects("GROUPS");
      } else if (lineBranchSource === "SYNC_SLIDER") {
        allTargetBranches = cachedSortedBranches.slice(sliderOffsetT1, sliderOffsetT1 + BAR_WINDOW);
      } else {
        allTargetBranches = cachedSortedBranches.filter(function(b) {
          return customPickedCodes.indexOf(b.code) !== -1;
        });
        if (!allTargetBranches.length && cachedSortedBranches.length) {
          allTargetBranches = cachedSortedBranches.slice(0, Math.min(5, cachedSortedBranches.length));
        }
      }

      // 控制窗格內永遠最多只顯示 5 家 (BAR_WINDOW = 5)，超過 5 家時由下方拉 BAR (#sliderCompare) 拖曳檢視
      var totalPicked = allTargetBranches.length;
      var maxCmpOffset = Math.max(0, totalPicked - BAR_WINDOW);
      if (compareSliderOffset > maxCmpOffset) compareSliderOffset = maxCmpOffset;
      if (compareSliderOffset < 0) compareSliderOffset = 0;

      var targetBranches = (lineBranchSource === "CUSTOM" && totalPicked > BAR_WINDOW)
        ? allTargetBranches.slice(compareSliderOffset, compareSliderOffset + BAR_WINDOW)
        : allTargetBranches.slice(0, BAR_WINDOW);

      var cmpWrap = el("compareSliderWrap");
      var cmpSlider = el("sliderCompare");
      var cmpRangeTxt = el("compareSliderRangeText");
      if (cmpWrap && cmpSlider && cmpRangeTxt) {
        cmpWrap.style.display = (lineBranchSource === "CUSTOM" || totalPicked > BAR_WINDOW) ? "flex" : "none";
        cmpSlider.max = String(maxCmpOffset);
        cmpSlider.value = String(compareSliderOffset);
        cmpSlider.disabled = totalPicked <= BAR_WINDOW;
        var sStart = totalPicked > 0 ? (compareSliderOffset + 1) : 0;
        var sEnd = Math.min(compareSliderOffset + BAR_WINDOW, totalPicked);
        if (totalPicked > BAR_WINDOW) {
          cmpRangeTxt.textContent = "目前顯示：第 " + sStart + "～" + sEnd + " 家 / 共 " + totalPicked + " 家";
        } else {
          cmpRangeTxt.textContent = "目前顯示：第 " + sStart + "～" + sEnd + " 家 (超過5家可拉動)";
        }
      }

      el("lineComparedBranchesSummary").textContent =
        "已勾選共 " + totalPicked + " 個單位｜目前窗格顯示（" + targetBranches.length + " 家）：" +
        targetBranches.map(function(b) { return b.isAggUnit ? (b.code + "總和") : (b.code + b.name.replace("分行", "")); }).join("、");

      // 1. 先渲染左圖：對應業務項目之【餘額柱狀圖 (去年同月/上月/當月)】
      renderComboBalanceBarAndGrowthChart(targetBranches, mInfo);

      // 2. 再渲染右圖：逐月折線圖 + 背景各月餘額柱狀圖 (維持窗格內僅顯示 6 個月份 MONTH_WINDOW = 6，下方拉 BAR 移動檢視)
      var allAvailableMonths = getAvailableTimelineMonths();
      var totalMonthsCount = allAvailableMonths.length;
      var maxMonthOffset = Math.max(0, totalMonthsCount - MONTH_WINDOW);
      if (lineMonthOffset > maxMonthOffset) lineMonthOffset = maxMonthOffset;
      if (lineMonthOffset < 0) lineMonthOffset = 0;

      var chartMonths = allAvailableMonths.slice(lineMonthOffset, lineMonthOffset + MONTH_WINDOW);

      var mSlider = el("sliderLineMonths");
      var mRangeTxt = el("monthSliderRangeText");
      if (mSlider && mRangeTxt) {
        mSlider.max = String(maxMonthOffset);
        mSlider.value = String(lineMonthOffset);
        mSlider.disabled = totalMonthsCount <= MONTH_WINDOW;
        if (chartMonths.length) {
          mRangeTxt.textContent = chartMonths[0] + " ～ " + chartMonths[chartMonths.length - 1] + " (" + chartMonths.length + "個月 / 共" + totalMonthsCount + "月)";
        } else {
          mRangeTxt.textContent = "無月份資料";
        }
      }

      var isLargeRegion = targetBranches[0] && targetBranches[0].isAggUnit;
      var rawDiv = (isLargeRegion && mInfo.unit === "萬") ? 100 : 1;
      var dispUnit = (rawDiv === 100) ? "百萬" : mInfo.unit;

      var modeTitle = lineModeKey === "MOM" ? "月增減率 MoM (%)" : (lineModeKey === "YOY" ? "年增減率 YoY (%)" : ("實際數值 (" + dispUnit + ")"));
      el("multiLineInfoBadge").textContent = "比較指標：【" + mInfo.name + "】×【左：三期餘額柱狀圖 ｜ 右：6個月" + modeTitle + "折線＋右側單位座標】";
      el("comboLineChartTitle").textContent = "逐月" + modeTitle + "折線 ＋ 各月" + mInfo.shortLabel + "柱狀圖";
      el("comboLineUnitBadge").textContent = "左軸：" + modeTitle + " ｜ 右軸：" + mInfo.shortLabel + "(" + dispUnit + ")";

      var datasets = targetBranches.map(function(b, bIdx) {
        var color = LINE_PALETTE[bIdx % LINE_PALETTE.length];
        var rawSeries = [];
        var series = chartMonths.map(function(ym) {
          var curVal = getBranchMetricValue(b, ym, lineMetricKey);
          rawSeries.push(Number((curVal / rawDiv).toFixed(1)));
          if (lineModeKey === "MOM") {
            var prevYm = getPrevMonth(ym);
            var prevVal = prevYm ? getBranchMetricValue(b, prevYm, lineMetricKey) : 0;
            if (!prevVal || prevVal <= 0) return 0;
            return Number((((curVal - prevVal) / prevVal) * 100).toFixed(1));
          } else if (lineModeKey === "YOY") {
            var yoyYm = getYoYMonth(ym);
            var yoyVal = yoyYm ? getBranchMetricValue(b, yoyYm, lineMetricKey) : 0;
            if (!yoyVal || yoyVal <= 0) return 0;
            return Number((((curVal - yoyVal) / yoyVal) * 100).toFixed(1));
          } else {
            return Number((curVal / rawDiv).toFixed(1));
          }
        });
        return {
          branch: b,
          label: b.isAggUnit ? (b.code + "總和") : (b.code + " " + b.name.replace("分行", "")),
          color: color,
          data: series,
          rawBars: rawSeries
        };
      });

      if (!datasets.length || !chartMonths.length) {
        box.innerHTML = '<div style="text-align:center;padding-top:90px;color:#647b92">請選擇至少一個單位進行比較</div>';
        return;
      }

      var minVal = Infinity, maxVal = -Infinity, maxRawBar = 1;
      datasets.forEach(function(ds) {
        ds.data.forEach(function(v) {
          if (v < minVal) minVal = v;
          if (v > maxVal) maxVal = v;
        });
        ds.rawBars.forEach(function(rv) {
          if (rv > maxRawBar) maxRawBar = rv;
        });
      });

      var isPct = (lineModeKey === "MOM" || lineModeKey === "YOY");
      if (isPct) {
        if (minVal > -2) minVal = -2;
        if (maxVal < 5) maxVal = 5;
        var padRange = (maxVal - minVal) * 0.14;
        minVal = Math.floor(minVal - padRange);
        maxVal = Math.ceil(maxVal + padRange);
      } else {
        minVal = 0;
        if (maxVal <= 0) maxVal = 10;
        maxVal = Math.ceil(maxVal * 1.15);
      }
      var valSpan = Math.max(maxVal - minVal, 1);
      // 右軸（各業務類別對應餘額/實績座標）上限：讓柱狀圖與右側座標軸刻度完全對應
      var maxBarAxis = Math.max(Math.ceil(maxRawBar * 1.25), 4);
      var showBgBars = el("showComboBarsInTimeline") ? el("showComboBarsInTimeline").checked : true;

      var legendHtml = '<div style="display:flex;gap:12px;justify-content:center;font-size:11.5px;margin-bottom:4px;flex-wrap:wrap;font-weight:700">';
      datasets.forEach(function(ds) {
        legendHtml += '<span style="display:inline-flex;align-items:center;gap:5px"><i style="width:14px;height:4px;border-radius:2px;background:' + ds.color + ';display:inline-block"></i><span style="color:#193653">' + ds.label + '</span></span>';
      });
      legendHtml += '</div>';

      var W = 640, H = 232, padL = 56, padR = 112, padT = 24, padB = 38;
      var plotW = W - padL - padR, plotH = H - padT - padB;
      var nCols = Math.max(chartMonths.length, 1);
      var colW = plotW / nCols;

      function monthIdxToX(idx) {
        return padL + idx * colW + colW / 2;
      }
      function valToY(v) {
        return padT + plotH - ((v - minVal) / valSpan) * plotH;
      }

      var svg = '<svg viewBox="0 0 ' + W + ' ' + H + '" style="width:100%;height:236px;overflow:visible">';

      // 頂部左軸與右軸單位座標標題
      svg += '<text x="' + (padL - 6) + '" y="12" text-anchor="start" font-size="9.5" font-weight="800" fill="#47627d">◀ 左軸：' + modeTitle + '</text>';
      svg += '<text x="' + (W - padR + 6) + '" y="12" text-anchor="start" font-size="9.5" font-weight="800" fill="#1d4ed8">右軸：' + mInfo.shortLabel + ' (' + dispUnit + ') ▶</text>';

      // 水平格線 ＋ 左軸(成長率%) ＋ 右軸(各業務類別對應單位座標，如「存款餘額 XXX萬」)
      for (var g = 0; g <= 4; g++) {
        var gVal = minVal + (valSpan * g / 4);
        var gy = padT + plotH - (plotH * g / 4);
        var rBarVal = Math.round(maxBarAxis * g / 4);
        var lblStr = isPct ? (gVal > 0 ? "+" + gVal.toFixed(1) + "%" : gVal.toFixed(1) + "%") : Math.round(gVal).toLocaleString();
        var rightAxisLbl = mInfo.shortLabel + " " + rBarVal.toLocaleString() + dispUnit;
        svg += '<line x1="' + padL + '" y1="' + gy.toFixed(1) + '" x2="' + (W - padR) + '" y2="' + gy.toFixed(1) + '" stroke="#e2e8f0" stroke-dasharray="3,3"/>';
        svg += '<text x="' + (padL - 6) + '" y="' + (gy + 4).toFixed(1) + '" text-anchor="end" font-size="9.5" font-weight="700" fill="#647b92">' + lblStr + '</text>';
        svg += '<text x="' + (W - padR + 6) + '" y="' + (gy + 4).toFixed(1) + '" text-anchor="start" font-size="9.5" font-weight="800" fill="#1d4ed8">' + rightAxisLbl + '</text>';
      }

      // 若勾選「在逐月折線圖底部同時顯示各月餘額柱狀圖」，柱高直接對應右側「業務類別單位座標軸 (0 ～ maxBarAxis)」
      if (showBgBars) {
        var subBarW = Math.max(4, Math.min(11, (colW * 0.68) / datasets.length));
        chartMonths.forEach(function(ym, mIdx) {
          var cx = monthIdxToX(mIdx);
          var totW = subBarW * datasets.length;
          var startBx = cx - totW / 2;
          datasets.forEach(function(ds, dIdx) {
            var rv = ds.rawBars[mIdx] || 0;
            var bh = Math.max(2, (rv / maxBarAxis) * plotH);
            var bx = startBx + dIdx * subBarW;
            var by = padT + plotH - bh;
            svg += '<rect x="' + bx.toFixed(1) + '" y="' + by.toFixed(1) + '" width="' + Math.max(2, subBarW - 1).toFixed(1) + '" height="' + bh.toFixed(1) + '" rx="2" fill="' + ds.color + '" opacity="0.28"><title>[' + ym + '] ' + ds.label + '｜' + mInfo.shortLabel + '：' + rv.toLocaleString() + ' ' + dispUnit + '</title></rect>';
          });
        });
      }

      // 若為 MoM / YoY 百分比模式，畫出醒目的 0.0% 基準線
      if (isPct && minVal <= 0 && maxVal >= 0) {
        var zeroY = valToY(0);
        svg += '<line x1="' + padL + '" y1="' + zeroY.toFixed(1) + '" x2="' + (W - padR) + '" y2="' + zeroY.toFixed(1) + '" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5,3"/>';
        svg += '<text x="' + (padL + 4) + '" y="' + (zeroY - 4).toFixed(1) + '" font-size="9" font-weight="800" fill="#dc2626">0% 基準線</text>';
      }

      // 標示目前選擇基準月份之垂直指示線
      var selMIdx = chartMonths.indexOf(selectedMonth);
      if (selMIdx !== -1) {
        var selX = monthIdxToX(selMIdx);
        svg += '<line x1="' + selX.toFixed(1) + '" y1="' + padT + '" x2="' + selX.toFixed(1) + '" y2="' + (padT + plotH) + '" stroke="#cbd5e1" stroke-width="1.8" stroke-dasharray="2,2"/>';
      }

      // 繪製各單位在 6 個月份窗格內的折線與節點
      datasets.forEach(function(ds) {
        var pts = [];
        ds.data.forEach(function(v, idx) {
          var px = monthIdxToX(idx);
          var py = valToY(v);
          pts.push(px.toFixed(1) + "," + py.toFixed(1));
        });
        svg += '<polyline fill="none" stroke="' + ds.color + '" stroke-width="2.5" points="' + pts.join(" ") + '"/>';

        ds.data.forEach(function(v, idx) {
          var px = monthIdxToX(idx);
          var py = valToY(v);
          var isCurM = chartMonths[idx] === selectedMonth;
          var r = isCurM ? 4.8 : 3.6;
          var vStr = isPct ? ((v >= 0 ? "+" : "") + v.toFixed(1) + "%") : (v.toLocaleString() + " " + dispUnit);
          var rawStr = ds.rawBars[idx].toLocaleString() + " " + dispUnit;
          svg += '<circle cx="' + px.toFixed(1) + '" cy="' + py.toFixed(1) + '" r="' + r + '" fill="' + ds.color + '" stroke="#fff" stroke-width="1.2"><title>[' + chartMonths[idx] + '] ' + ds.label + '｜餘額: ' + rawStr + '｜' + modeTitle + ': ' + vStr + '</title></circle>';
          if (isCurM || idx === chartMonths.length - 1) {
            svg += '<text x="' + px.toFixed(1) + '" y="' + (py - 7).toFixed(1) + '" text-anchor="middle" font-size="9.5" font-weight="800" fill="' + ds.color + '">' + vStr + '</text>';
          }
        });
      });

      // X 軸 6 個月份完整標籤
      chartMonths.forEach(function(ym, idx) {
        var px = monthIdxToX(idx);
        var isSel = ym === selectedMonth;
        svg += '<text x="' + px.toFixed(1) + '" y="' + (H - 12) + '" text-anchor="middle" font-size="' + (isSel ? "11" : "10.5") + '" font-weight="' + (isSel ? "900" : "700") + '" fill="' + (isSel ? "#082d5b" : "#334155") + '">' + ym + '</text>';
      });

      svg += '</svg>';
      mountChartWithZoom("chartMultiBranchLine", legendHtml + svg);

      // 3. 同步更新下方「同圖比較單位：當月餘額 × 月增減 MoM × 年增減 YoY 對照表」
      var momYm = getPrevMonth(selectedMonth);
      var yoyYm = getYoYMonth(selectedMonth);
      el("thCurMetric").textContent = mInfo.name + " (" + selectedMonth + ")";
      el("thMomBase").textContent = "上月 (" + (momYm || "無") + ")";
      el("thYoyBase").textContent = "去年同月 (" + (yoyYm || "無") + ")";

      var dtBody = document.querySelector("#multiBranchCompareDetailTable tbody");
      dtBody.innerHTML = "";
      datasets.forEach(function(ds) {
        var b = ds.branch;
        var curV = getBranchMetricValue(b, selectedMonth, lineMetricKey);
        var momV = momYm ? getBranchMetricValue(b, momYm, lineMetricKey) : 0;
        var yoyV = yoyYm ? getBranchMetricValue(b, yoyYm, lineMetricKey) : 0;

        var momDiff = momYm ? (curV - momV) : 0;
        var yoyDiff = yoyYm ? (curV - yoyV) : 0;
        var momDiffStr = momYm ? ((momDiff >= 0 ? "+" : "") + formatMetricVal(momDiff, lineMetricKey)) : "—";
        var yoyDiffStr = yoyYm ? ((yoyDiff >= 0 ? "+" : "") + formatMetricVal(yoyDiff, lineMetricKey)) : "—";

        var tr = document.createElement("tr");
        tr.innerHTML =
          '<td><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:' + ds.color + ';margin-right:6px"></span><b>' + b.code + ' ' + b.name + '</b></td>' +
          '<td><span class="demo">' + b.region + '</span> ' + b.subRegion + ' / ' + b.group + '</td>' +
          '<td><b>' + formatMetricVal(curV, lineMetricKey) + '</b></td>' +
          '<td>' + (momYm ? formatMetricVal(momV, lineMetricKey) : "—") + '</td>' +
          '<td style="font-weight:700;color:' + (momDiff >= 0 ? "#15803d" : "#b91c1c") + '">' + momDiffStr + '</td>' +
          '<td>' + deltaBadgeHtml("MoM", curV, momV) + '</td>' +
          '<td>' + (yoyYm ? formatMetricVal(yoyV, lineMetricKey) : "—") + '</td>' +
          '<td style="font-weight:700;color:' + (yoyDiff >= 0 ? "#15803d" : "#b91c1c") + '">' + yoyDiffStr + '</td>' +
          '<td>' + deltaBadgeHtml("YoY", curV, yoyV) + '</td>';
        tr.addEventListener("click", function() {
          if (b.isAggUnit) {
            if (b.aggType === "REGIONS" && currentRole === "HQ") {
              el("warRegionFilter").value = b.code;
              drawWarRoom();
              toast("🗺️ 已篩選檢視【" + b.code + "】轄下各分行");
            }
            return;
          }
          insideBranchCode = b.code;
          el("insideBranchSelect").value = insideBranchCode;
          renderBranchInsidePanel();
          switchWarSubTab("branch-inside");
          toast("🔍 已切換檢視【" + b.code + " " + b.name + "】內部狀況");
        });
        dtBody.appendChild(tr);
      });
    }

    // =========================================================================
    // 4. 戰情室主渲染函數 (涵蓋 MoM / YoY 與 5 大視角)
    // =========================================================================
    function drawWarRoom() {
      selectedMonth = el("warMonthSelect").value;
      var momMonth = getPrevMonth(selectedMonth);
      var yoyMonth = getYoYMonth(selectedMonth);

      el("warComparisonInfo").textContent =
        "基準月：" + selectedMonth +
        " ｜ 月增減 (MoM) 對照：" + (momMonth || "無(首月)") +
        " ｜ 年增減 (YoY) 對照：" + (yoyMonth || "無(首年)");

      var allowedBranches = getAllowedBranches();
      el("branchCountBadge").textContent = allowedBranches.length;

      var curAgg = aggregateBranchesAtMonth(allowedBranches, selectedMonth);
      var momAgg = aggregateBranchesAtMonth(allowedBranches, momMonth);
      var yoyAgg = aggregateBranchesAtMonth(allowedBranches, yoyMonth);

      // --- 頂部 8 張 KPI 卡片 (含 MoM / YoY 增減率) ---
      el("kpiT1Deposit").textContent = formatWanToReadable(curAgg.depW);
      el("deltaT1Deposit").innerHTML =
        deltaBadgeHtml("月增減 MoM", curAgg.depW, momAgg.depW) +
        deltaBadgeHtml("年增減 YoY", curAgg.depW, yoyAgg.depW);

      var utilRate = curAgg.limitW > 0 ? Math.round((curAgg.loanW * 100) / curAgg.limitW) : 0;
      el("kpiT1Loan").textContent = formatWanToReadable(curAgg.loanW) + " (動用" + utilRate + "%)";
      el("deltaT1Loan").innerHTML =
        deltaBadgeHtml("月增減 MoM", curAgg.loanW, momAgg.loanW) +
        deltaBadgeHtml("年增減 YoY", curAgg.loanW, yoyAgg.loanW);

      el("kpiT1Fund").textContent = formatWanToReadable(curAgg.fundW) + " (新購+" + formatWanToReadable(curAgg.fundNewW) + ")";
      el("deltaT1Fund").innerHTML =
        deltaBadgeHtml("月增減 MoM", curAgg.fundW, momAgg.fundW) +
        deltaBadgeHtml("年增減 YoY", curAgg.fundW, yoyAgg.fundW);

      var gebRate = curAgg.custCount > 0 ? Math.round((curAgg.gebCount * 100) / curAgg.custCount) : 0;
      el("kpiT1Geb").textContent = gebRate + "% (" + curAgg.gebCount + "/" + curAgg.custCount + "戶)";
      el("deltaT1Contrib").innerHTML =
        deltaBadgeHtml("貢獻 MoM", curAgg.t1Contrib, momAgg.t1Contrib) +
        deltaBadgeHtml("貢獻 YoY", curAgg.t1Contrib, yoyAgg.t1Contrib);

      el("kpiT2Cases").textContent = curAgg.visits + " 訪 (" + curAgg.reports + "報 / " + curAgg.closed + "成 / " + curAgg.tracking + "追)";
      el("deltaT2Cases").innerHTML =
        deltaBadgeHtml("成案件數 MoM", curAgg.closed, momAgg.closed) +
        deltaBadgeHtml("成案件數 YoY", curAgg.closed, yoyAgg.closed);

      el("kpiT2ReportAmt").textContent = formatWanToReadable(curAgg.repW);
      el("deltaT2ReportAmt").innerHTML =
        deltaBadgeHtml("月增減 MoM", curAgg.repW, momAgg.repW) +
        deltaBadgeHtml("年增減 YoY", curAgg.repW, yoyAgg.repW);

      el("kpiT2CloseAmt").textContent = formatWanToReadable(curAgg.clsW);
      el("deltaT2CloseAmt").innerHTML =
        deltaBadgeHtml("月增減 MoM", curAgg.clsW, momAgg.clsW) +
        deltaBadgeHtml("年增減 YoY", curAgg.clsW, yoyAgg.clsW);

      el("kpiT2Score").textContent = curAgg.weight.toFixed(1) + " 分 (專案+" + curAgg.points + "點)";
      el("deltaT2Score").innerHTML =
        deltaBadgeHtml("權重 MoM", curAgg.weight, momAgg.weight) +
        deltaBadgeHtml("權重 YoY", curAgg.weight, yoyAgg.weight);

      // =====================================================================
      // 視角 1：轄下各分行績效與月/年增減總覽 (總處5大業務分區總和 + 5家分行拉BAR + 業務餘額柱狀×成長率折線圖)
      // =====================================================================
      renderHqRegionTotalsStrip();

      var sortedBranches = allowedBranches.slice().sort(function(a, b) {
        var ma = a.m[selectedMonth], mb = b.m[selectedMonth];
        var sa = (ma[5] + ma[14]) + ma[11] * 0.2;
        var sb = (mb[5] + mb[14]) + mb[11] * 0.2;
        return sb - sa;
      });
      cachedSortedBranches = sortedBranches;

      render5BranchBarCharts();
      renderCustomBranchChips();
      renderMultiBranchCompareSection();

      var scBody = document.querySelector("#branchScorecardTable tbody");
      scBody.innerHTML = "";
      sortedBranches.forEach(function(b, idx) {
        var cur = b.m[selectedMonth];
        var mom = momMonth ? b.m[momMonth] : null;
        var yoy = yoyMonth ? b.m[yoyMonth] : null;
        var gebPct = b.custCount > 0 ? Math.round((b.gebCount * 100) / b.custCount) : 0;
        var curTotC = cur[5] + cur[14];
        var yoyTotC = yoy ? (yoy[5] + yoy[14]) : 0;

        var tr = document.createElement("tr");
        tr.setAttribute("data-bcode", b.code);
        var rankStr = idx === 0 ? "🥇 1" : (idx === 1 ? "🥈 2" : (idx === 2 ? "🥉 3" : (idx + 1)));
        tr.innerHTML =
          "<td><b>" + rankStr + "</b></td>" +
          "<td><b>" + b.code + " " + b.name + "</b></td>" +
          "<td><span class='demo'>" + b.region + "</span> " + b.subRegion + " / " + b.group + "</td>" +
          "<td><b>" + formatWanToReadable(cur[0]) + "</b><div class='delta-row'>" + deltaBadgeHtml("MoM", cur[0], mom ? mom[0] : 0) + deltaBadgeHtml("YoY", cur[0], yoy ? yoy[0] : 0) + "</div></td>" +
          "<td><b>" + formatWanToReadable(cur[1]) + "</b><div class='delta-row'>" + deltaBadgeHtml("MoM", cur[1], mom ? mom[1] : 0) + deltaBadgeHtml("YoY", cur[1], yoy ? yoy[1] : 0) + "</div></td>" +
          "<td><b>" + formatWanToReadable(cur[3]) + "</b><div class='delta-row'>" + deltaBadgeHtml("MoM", cur[3], mom ? mom[3] : 0) + deltaBadgeHtml("YoY", cur[3], yoy ? yoy[3] : 0) + "</div></td>" +
          "<td>" + gebPct + "% (" + b.gebCount + "/" + b.custCount + ")</td>" +
          "<td><b>" + cur[6] + "</b>訪 / " + cur[7] + "報 / <b style='color:var(--green)'>" + cur[8] + "成</b> / <span style='color:#d97706;font-weight:700'>" + cur[9] + "追</span></td>" +
          "<td>" + formatWanToReadable(cur[10]) + "<div class='delta-row'>" + deltaBadgeHtml("MoM", cur[10], mom ? mom[10] : 0) + "</div></td>" +
          "<td><b style='color:var(--green)'>" + formatWanToReadable(cur[11]) + "</b><div class='delta-row'>" + deltaBadgeHtml("MoM", cur[11], mom ? mom[11] : 0) + deltaBadgeHtml("YoY", cur[11], yoy ? yoy[11] : 0) + "</div></td>" +
          "<td><b>" + (cur[12] / 10).toFixed(1) + " 分</b> (+" + cur[13] + "點)<div class='delta-row'>" + deltaBadgeHtml("MoM", cur[12], mom ? mom[12] : 0) + "</div></td>" +
          "<td><b>" + curTotC.toLocaleString() + "</b><div class='delta-row'>" + deltaBadgeHtml("YoY", curTotC, yoyTotC) + "</div></td>";

        tr.addEventListener("click", function() {
          insideBranchCode = this.getAttribute("data-bcode");
          el("insideBranchSelect").value = insideBranchCode;
          renderBranchInsidePanel();
          switchWarSubTab("branch-inside");
          toast("🔍 已切換檢視【" + insideBranchCode + " 分行】內部狀況");
        });
        scBody.appendChild(tr);
      });

      // =====================================================================
      // 視角 2：2025/01 ～ 2026/11 (23個月) 歷史趨勢與增減明細
      // =====================================================================
      var histDepM = [], histLoanM = [], histFundM = [], histRepM = [], histClsM = [];
      var histMonthSeries = allMonths.map(function(ym) {
        var agg = aggregateBranchesAtMonth(allowedBranches, ym);
        histDepM.push(Math.round(agg.depW / 100));   // 百萬
        histLoanM.push(Math.round(agg.loanW / 100)); // 百萬
        histFundM.push(Math.round(agg.fundW / 100)); // 百萬
        histRepM.push(Math.round(agg.repW / 100));   // 百萬
        histClsM.push(Math.round(agg.clsW / 100));   // 百萬
        return { ym: ym, agg: agg };
      });

      renderSvgLineChart("chartHistoryT1", allMonths, [
        { label: "總存款(百萬)", data: histDepM, color: "#2878e5" },
        { label: "總授信(百萬)", data: histLoanM, color: "#20a55a" },
        { label: "總基金(百萬)", data: histFundM, color: "#f59f00" }
      ]);

      renderSvgLineChart("chartHistoryT2", allMonths, [
        { label: "通報總額(百萬)", data: histRepM, color: "#3b82f6" },
        { label: "成案總額(百萬)", data: histClsM, color: "#16834a" }
      ]);

      var mhBody = document.querySelector("#monthlyHistoryTable tbody");
      mhBody.innerHTML = "";
      for (var mIdx = histMonthSeries.length - 1; mIdx >= 0; mIdx--) {
        var item = histMonthSeries[mIdx];
        var ym = item.ym;
        var a = item.agg;
        var prevA = mIdx > 0 ? histMonthSeries[mIdx - 1].agg : null;
        var yoyYm = getYoYMonth(ym);
        var yoyA = yoyYm ? aggregateBranchesAtMonth(allowedBranches, yoyYm) : null;

        var trM = document.createElement("tr");
        if (ym === selectedMonth) trM.className = "selected-row";
        trM.innerHTML =
          "<td><b>" + ym + "</b></td>" +
          "<td><b>" + formatWanToReadable(a.depW) + "</b> " + deltaBadgeHtml("MoM", a.depW, prevA ? prevA.depW : 0) + " " + deltaBadgeHtml("YoY", a.depW, yoyA ? yoyA.depW : 0) + "</td>" +
          "<td><b>" + formatWanToReadable(a.loanW) + "</b> " + deltaBadgeHtml("MoM", a.loanW, prevA ? prevA.loanW : 0) + " " + deltaBadgeHtml("YoY", a.loanW, yoyA ? yoyA.loanW : 0) + "</td>" +
          "<td><b>" + formatWanToReadable(a.fundW) + "</b> " + deltaBadgeHtml("MoM", a.fundW, prevA ? prevA.fundW : 0) + " " + deltaBadgeHtml("YoY", a.fundW, yoyA ? yoyA.fundW : 0) + "</td>" +
          "<td>" + a.visits + "訪 / " + a.reports + "報 / <b>" + a.closed + "成</b> / " + a.tracking + "追</td>" +
          "<td>" + formatWanToReadable(a.repW) + " " + deltaBadgeHtml("MoM", a.repW, prevA ? prevA.repW : 0) + "</td>" +
          "<td><b style='color:var(--green)'>" + formatWanToReadable(a.clsW) + "</b> " + deltaBadgeHtml("MoM", a.clsW, prevA ? prevA.clsW : 0) + " " + deltaBadgeHtml("YoY", a.clsW, yoyA ? yoyA.clsW : 0) + "</td>" +
          "<td><b>" + a.weight.toFixed(1) + " 分</b></td>" +
          "<td>+" + a.points + " 點</td>" +
          "<td><b>" + a.totalContrib.toLocaleString() + "</b> " + deltaBadgeHtml("YoY", a.totalContrib, yoyA ? yoyA.totalContrib : 0) + "</td>";
        mhBody.appendChild(trM);
      }

      // =====================================================================
      // 視角 3：各業務分區 × 組別表現對照
      // =====================================================================
      var regionNames = currentRole === "REGION" ? [lockedRegion] : ["北區", "桃竹苗區", "中區", "南區"];
      var regCurList = regionNames.map(function(rg) {
        var sub = allowedBranches.filter(function(b) { return b.region === rg; });
        return {
          name: rg,
          cur: aggregateBranchesAtMonth(sub, selectedMonth),
          mom: aggregateBranchesAtMonth(sub, momMonth),
          yoy: aggregateBranchesAtMonth(sub, yoyMonth)
        };
      });
      renderSvgBarChart("chartRegionCompare", regCurList.map(function(x) { return x.name; }), [
        { label: "總存款(百萬)", data: regCurList.map(function(x) { return Math.round(x.cur.depW / 100); }), color: "#2878e5" },
        { label: "總授信(百萬)", data: regCurList.map(function(x) { return Math.round(x.cur.loanW / 100); }), color: "#20a55a" },
        { label: "成案金額(百萬)", data: regCurList.map(function(x) { return Math.round(x.cur.clsW / 100); }), color: "#f59f00" }
      ]);

      var groupNames = ["第一組", "第二組", "第三組", "第四組", "第五組"];
      var grpCurList = groupNames.map(function(gp) {
        var sub = allowedBranches.filter(function(b) { return b.group === gp; });
        return {
          name: gp,
          cur: aggregateBranchesAtMonth(sub, selectedMonth),
          mom: aggregateBranchesAtMonth(sub, momMonth),
          yoy: aggregateBranchesAtMonth(sub, yoyMonth)
        };
      });
      renderSvgBarChart("chartGroupCompare", grpCurList.map(function(x) { return x.name; }), [
        { label: "通報商機(百萬)", data: grpCurList.map(function(x) { return Math.round(x.cur.repW / 100); }), color: "#3b82f6" },
        { label: "實際成案(百萬)", data: grpCurList.map(function(x) { return Math.round(x.cur.clsW / 100); }), color: "#16834a" }
      ]);

      var rsBody = document.querySelector("#regionSummaryTable tbody");
      rsBody.innerHTML = "";
      function addSummaryRow(prefix, item) {
        var c = item.cur, m = item.mom, y = item.yoy;
        if (c.branchCount === 0) return;
        var gPct = c.custCount > 0 ? Math.round((c.gebCount * 100) / c.custCount) + "%" : "0%";
        var tr = document.createElement("tr");
        tr.innerHTML =
          "<td><b>" + prefix + item.name + "</b></td>" +
          "<td>" + c.branchCount + " 家</td>" +
          "<td>" + c.custCount + " 戶</td>" +
          "<td><b>" + formatWanToReadable(c.depW) + "</b> " + deltaBadgeHtml("MoM", c.depW, m.depW) + " " + deltaBadgeHtml("YoY", c.depW, y.depW) + "</td>" +
          "<td><b>" + formatWanToReadable(c.loanW) + "</b> " + deltaBadgeHtml("MoM", c.loanW, m.loanW) + " " + deltaBadgeHtml("YoY", c.loanW, y.loanW) + "</td>" +
          "<td><b>" + formatWanToReadable(c.fundW) + "</b> " + deltaBadgeHtml("MoM", c.fundW, m.fundW) + " " + deltaBadgeHtml("YoY", c.fundW, y.fundW) + "</td>" +
          "<td>" + gPct + "</td>" +
          "<td>" + c.visits + "訪 / " + c.reports + "報 / <b>" + c.closed + "成</b> / " + c.tracking + "追</td>" +
          "<td>" + formatWanToReadable(c.repW) + "</td>" +
          "<td><b style='color:var(--green)'>" + formatWanToReadable(c.clsW) + "</b> " + deltaBadgeHtml("MoM", c.clsW, m.clsW) + " " + deltaBadgeHtml("YoY", c.clsW, y.clsW) + "</td>" +
          "<td><b>" + c.weight.toFixed(1) + " 分</b></td>" +
          "<td><b>" + c.totalContrib.toLocaleString() + "</b> " + deltaBadgeHtml("YoY", c.totalContrib, y.totalContrib) + "</td>";
        rsBody.appendChild(tr);
      }
      regCurList.forEach(function(x) { addSummaryRow("🗺️ ", x); });
      grpCurList.forEach(function(x) { addSummaryRow("🏢 ", x); });

      // =====================================================================
      // 視角 4：分行內部狀況檢視 (科別 / 行員 / 客戶 / 案件)
      // =====================================================================
      renderBranchInsidePanel();

      // =====================================================================
      // 視角 5：轄下重大未結追蹤案 (Pipeline) 督導表
      // =====================================================================
      var allowedCodes = {};
      allowedBranches.forEach(function(b) { allowedCodes[b.code] = true; });
      var pendingCases = table2Records.filter(function(r) {
        return allowedCodes[r.branch] && r.closeStatus !== "有" && r.hasReport === "有";
      }).sort(function(a, b) { return parseMoney(b.reportAmt) - parseMoney(a.reportAmt); });

      var pipeBody = document.querySelector("#pipelineTable tbody");
      pipeBody.innerHTML = "";
      if (!pendingCases.length) {
        pipeBody.innerHTML = '<tr><td colspan="12" style="text-align:center;color:#16834a;font-weight:700">✅ 目前轄下無待督導之未結追蹤案件</td></tr>';
      } else {
        pendingCases.forEach(function(r) {
          var tr = document.createElement("tr");
          var amtNum = parseMoney(r.reportAmt);
          var prio = amtNum >= 100000000 ? '<span class="demo red">🔥 特大案 (≥1億)</span>' : '<span class="demo amber">⚡ 重點追蹤</span>';
          tr.innerHTML =
            "<td>" + prio + "</td>" +
            "<td><b>" + r.branch + " " + r.branchName + "</b> (" + r.region + "/" + r.group + ")</td>" +
            "<td>" + r.dept + "科｜" + r.clerkId + " " + r.clerkName + "</td>" +
            "<td><b>" + r.caseId + "</b> (" + r.ym + ")</td>" +
            "<td><b>" + r.custShort + "</b></td>" +
            "<td><b>" + r.bizType + "</b></td>" +
            "<td style='color:#c5353d;font-weight:900'>" + r.reportAmt + "</td>" +
            '<td><span class="demo amber">' + r.closeStatus + "</span></td>" +
            "<td>" + r.weight.toFixed(1) + "</td>" +
            "<td><b>" + r.progressNote + "</b></td>" +
            "<td>" + r.units + "</td>" +
            "<td>" + r.action + " (" + r.due + ")</td>";
          tr.addEventListener("click", function() {
            currentCustId = r.custId;
            currentCaseId = r.caseId;
            renderSelectors();
            loadCurrentSelectionToUI();
            page("interview");
            toast("已載入待督導追蹤案件 " + r.caseId);
          });
          pipeBody.appendChild(tr);
        });
      }
    }

    // 渲染單一分行內部狀況面板 (營業/授信/理財科別、行員、客戶、案件 + 分行MoM/YoY)
    function renderBranchInsidePanel() {
      var bCode = el("insideBranchSelect").value || insideBranchCode;
      insideBranchCode = bCode;
      var bObj = null;
      for (var i = 0; i < branchMonthlyList.length; i++) {
        if (branchMonthlyList[i].code === bCode) { bObj = branchMonthlyList[i]; break; }
      }
      if (!bObj) return;

      var momMonth = getPrevMonth(selectedMonth);
      var yoyMonth = getYoYMonth(selectedMonth);
      var cur = bObj.m[selectedMonth];
      var mom = momMonth ? bObj.m[momMonth] : null;
      var yoy = yoyMonth ? bObj.m[yoyMonth] : null;

      el("insideBranchMeta").textContent =
        bObj.region + " ／ 小分區：" + bObj.subRegion + " ／ " + bObj.group + " ／ 分區屬性：" + bObj.category + " ／ 管轄客戶：" + bObj.custCount + "戶";

      el("insideBranchKpiRow").innerHTML =
        '<div class="metric"><span class="m-lbl">🏦 本分行總存款 (' + selectedMonth + ')</span><b class="m-val">' + formatWanToReadable(cur[0]) + '</b><div class="delta-row">' + deltaBadgeHtml("MoM", cur[0], mom ? mom[0] : 0) + deltaBadgeHtml("YoY", cur[0], yoy ? yoy[0] : 0) + '</div></div>' +
        '<div class="metric"><span class="m-lbl">🤝 本分行總授信 (' + selectedMonth + ')</span><b class="m-val">' + formatWanToReadable(cur[1]) + '</b><div class="delta-row">' + deltaBadgeHtml("MoM", cur[1], mom ? mom[1] : 0) + deltaBadgeHtml("YoY", cur[1], yoy ? yoy[1] : 0) + '</div></div>' +
        '<div class="metric"><span class="m-lbl">🚀 本分行當月成案金額</span><b class="m-val" style="color:var(--green)">' + formatWanToReadable(cur[11]) + '</b><div class="delta-row">' + deltaBadgeHtml("MoM", cur[11], mom ? mom[11] : 0) + deltaBadgeHtml("YoY", cur[11], yoy ? yoy[11] : 0) + '</div></div>' +
        '<div class="metric"><span class="m-lbl">🏆 本分行階段權重積分</span><b class="m-val">' + (cur[12] / 10).toFixed(1) + ' 分 (+' + cur[13] + '點)</b><div class="delta-row">' + deltaBadgeHtml("MoM", cur[12], mom ? mom[12] : 0) + deltaBadgeHtml("YoY", cur[12], yoy ? yoy[12] : 0) + '</div></div>';

      // 分行內三大科別表現 (營業科 / 授信科 / 理財科)
      var repTotal = cur[10], clsTotal = cur[11];
      renderSvgBarChart("chartInsideDepts", ["營業科", "授信科", "理財科"], [
        { label: "通報金額(萬)", data: [Math.round(repTotal * 0.35), Math.round(repTotal * 0.45), Math.round(repTotal * 0.20)], color: "#3b82f6" },
        { label: "成案金額(萬)", data: [Math.round(clsTotal * 0.36), Math.round(clsTotal * 0.44), Math.round(clsTotal * 0.20)], color: "#16834a" }
      ]);

      // 該分行案件與客戶明細
      var bCusts = table1Customers.filter(function(c) { return c.branch === bCode; });
      var bCases = table2Records.filter(function(r) { return r.branch === bCode; });

      var clerkLabels = bCases.map(function(r) { return r.clerkId + " " + r.clerkName + "(" + r.dept + ")"; });
      var clerkRep = bCases.map(function(r) { return Math.round(parseMoney(r.reportAmt) / 10000); });
      var clerkCls = bCases.map(function(r) { return Math.round(parseMoney(r.closeAmt) / 10000); });
      renderSvgBarChart("chartInsideClerks", clerkLabels, [
        { label: "通報商機(萬)", data: clerkRep, color: "#2878e5" },
        { label: "實際成案(萬)", data: clerkCls, color: "#16834a" }
      ]);

      var tb1 = document.querySelector("#drillT1Table tbody");
      tb1.innerHTML = "";
      bCusts.forEach(function(c) {
        var tr = document.createElement("tr");
        var gebCls = c.geb === "已申辦" ? "green" : (c.geb === "申請中" ? "amber" : "red");
        tr.innerHTML =
          "<td><b>" + c.id + " " + c.shortName + "</b></td>" +
          "<td>" + c.fullName + "</td>" +
          "<td>" + c.deposit + "</td>" +
          "<td>" + c.loanBalance + " / " + c.loanLimit + "</td>" +
          "<td>" + c.fundBalance + "</td>" +
          '<td><span class="demo ' + gebCls + '">' + c.geb + "</span></td>" +
          "<td><b>" + c.contrib + "</b></td>";
        tr.addEventListener("click", function() {
          currentCustId = c.id;
          renderSelectors();
          loadCurrentSelectionToUI();
          page("customer");
          toast("已載入客戶 " + c.shortName);
        });
        tb1.appendChild(tr);
      });

      var tb2 = document.querySelector("#drillT2TableBodyOnly tbody");
      tb2.innerHTML = "";
      bCases.forEach(function(r) {
        var tr = document.createElement("tr");
        var stCls = r.closeStatus === "有" ? "green" : (r.closeStatus === "追蹤" ? "amber" : "");
        tr.innerHTML =
          "<td><b>" + r.caseId + "</b></td>" +
          "<td>" + r.dept + "科｜" + r.clerkId + " " + r.clerkName + "</td>" +
          "<td><b>" + r.custShort + "</b></td>" +
          "<td>" + r.bizType + "</td>" +
          "<td>" + r.reportAmt + "</td>" +
          '<td><span class="demo ' + stCls + '">' + r.closeStatus + "</span></td>" +
          "<td><b>" + r.closeAmt + "</b></td>" +
          "<td><b>" + r.weight.toFixed(1) + "</b> (+" + r.points + "點)</td>" +
          "<td>" + r.progressNote + "</td>";
        tr.addEventListener("click", function() {
          currentCustId = r.custId;
          currentCaseId = r.caseId;
          renderSelectors();
          loadCurrentSelectionToUI();
          page("interview");
          toast("已載入案件 " + r.caseId);
        });
        tb2.appendChild(tr);
      });
    }

    // =========================================================================
    // 5. 客戶概況、業務爭攬與報告生成連動 (依權責過濾客戶清單)
    // =========================================================================
    function getRbacCustomers() {
      return table1Customers.filter(function(c) {
        if (currentRole === "REGION") return c.region === lockedRegion;
        if (currentRole === "BRANCH") return c.branch === lockedBranch;
        return true;
      });
    }

    function renderSelectors() {
      var cSel = el("customerSelect");
      cSel.innerHTML = "";
      var custList = getRbacCustomers();
      if (!custList.length) custList = table1Customers;

      var foundC = custList.some(function(c) { return c.id === currentCustId; });
      if (!foundC) currentCustId = custList[0].id;

      custList.forEach(function(c) {
        var opt = document.createElement("option");
        opt.value = c.id;
        opt.textContent = c.id + "｜" + c.shortName + " — " + c.fullName + " (" + c.branch + " " + c.branchName + " / GEB:" + c.geb + ")";
        if (c.id === currentCustId) opt.selected = true;
        cSel.appendChild(opt);
      });
      renderCaseSelectorForCustomer(currentCustId);
    }

    function getCustomerById(custId) {
      for (var i = 0; i < table1Customers.length; i++) {
        if (table1Customers[i].id === custId) return table1Customers[i];
      }
      return table1Customers[0];
    }

    function getCasesByCustomer(custId) {
      return table2Records.filter(function(r) { return r.custId === custId; });
    }

    function getCaseById(caseId) {
      for (var i = 0; i < table2Records.length; i++) {
        if (table2Records[i].caseId === caseId) return table2Records[i];
      }
      return null;
    }

    function renderCaseSelectorForCustomer(custId) {
      var kSel = el("caseSelect");
      kSel.innerHTML = "";
      var cases = getCasesByCustomer(custId);
      if (!cases.length) {
        currentCaseId = "";
        return;
      }
      var found = cases.some(function(r) { return r.caseId === currentCaseId; });
      if (!found) currentCaseId = cases[0].caseId;
      cases.forEach(function(r) {
        var o = document.createElement("option");
        o.value = r.caseId;
        o.textContent = r.caseId + "｜" + r.branch + " " + r.branchName + " " + r.clerkName + " [" + r.bizType + " " + r.reportAmt + " / 狀態:" + r.closeStatus + "]";
        if (r.caseId === currentCaseId) o.selected = true;
        kSel.appendChild(o);
      });
    }

    function loadCurrentSelectionToUI() {
      var c = getCustomerById(currentCustId);
      if (!c) return;

      el("custDateBadge").textContent = "資料月份：" + c.date;
      el("custCodeName").value = c.id + " / " + c.shortName;
      el("cust").value = c.fullName;
      el("uni").value = c.uni;
      el("industry").value = c.industry;
      el("rating").value = String(c.rating);
      el("custBranchInfo").value = c.region + " / " + c.group + " / " + c.branch + " " + c.branchName + " (歸屬:" + c.tier + ")";
      el("custPhone").value = c.phone || "";
      el("custRM").value = c.rm || "";
      el("custAddr").value = c.addr || "";
      el("aiSummaryBox").textContent = c.aiSummary || "";

      var depNum = parseMoney(c.deposit);
      var fxDepNum = parseMoney(c.fxDeposit);
      var limitNum = parseMoney(c.loanLimit);
      var loanNum = parseMoney(c.loanBalance);
      var fundNum = parseMoney(c.fundBalance);
      var fundMNum = parseMoney(c.fundMonth);

      el("pDeposit").textContent = formatNT(depNum);
      el("pDepositRaw").textContent = "原表數值：" + c.deposit;
      el("pFxDeposit").textContent = formatNT(fxDepNum);
      el("pFxDepositRaw").textContent = "原表數值：" + c.fxDeposit;
      el("pLoan").textContent = c.loanBalance + " ／ " + c.loanLimit;
      var utilRate = limitNum > 0 ? Math.round((loanNum / limitNum) * 100) : 0;
      el("pLoanRate").textContent = "額度動用率：" + utilRate + "%";
      el("pFund").textContent = formatNT(fundNum);
      el("pFundMonth").textContent = "本月新購：" + c.fundMonth + " (" + formatNT(fundMNum) + ")";
      el("pGeb").textContent = c.geb;
      el("pPayroll").textContent = "薪轉戶：" + c.payroll;
      el("pContrib").textContent = c.contrib + " 點";
      el("pFxTrade").textContent = "匯兌：" + c.fxStatus + "｜進出口：" + c.tradeStatus;

      var gebBadge = el("gebBadge");
      gebBadge.textContent = "企業網銀 GEB：" + c.geb;
      gebBadge.className = "demo " + (c.geb === "已申辦" ? "green" : (c.geb === "申請中" ? "amber" : "red"));

      // 該客戶案件列表
      var tbody = document.querySelector("#custCasesTable tbody");
      tbody.innerHTML = "";
      var cases = getCasesByCustomer(c.id);
      cases.forEach(function(r) {
        var tr = document.createElement("tr");
        if (r.caseId === currentCaseId) tr.className = "selected-row";
        var statusBadge = r.closeStatus === "有" ? '<span class="demo green">有 (已成案)</span>' : '<span class="demo amber">追蹤中</span>';
        tr.innerHTML =
          "<td><b>" + r.caseId + "</b></td>" +
          "<td>" + r.ym + "</td>" +
          "<td>" + r.region + " / " + r.group + " / " + r.branch + " " + r.branchName + "</td>" +
          "<td>" + r.dept + "</td>" +
          "<td>" + r.clerkId + " " + r.clerkName + "</td>" +
          "<td>" + r.visitType + "</td>" +
          "<td>" + r.hasReport + "</td>" +
          "<td><b>" + r.bizType + "</b></td>" +
          "<td>" + r.reportAmt + "</td>" +
          "<td>" + statusBadge + "</td>" +
          "<td><b>" + r.closeAmt + "</b></td>" +
          "<td>" + r.points + (r.pointsNote ? " (" + r.pointsNote + ")" : "") + "</td>" +
          "<td><b>" + r.weight.toFixed(1) + "</b></td>" +
          "<td>" + r.contrib + "</td>" +
          "<td>" + r.progressNote + "</td>";
        tr.addEventListener("click", function() {
          currentCaseId = r.caseId;
          el("caseSelect").value = currentCaseId;
          loadCurrentSelectionToUI();
        });
        tbody.appendChild(tr);
      });

      var rec = getCaseById(currentCaseId);
      if (rec) {
        el("currentCaseBadge").textContent = rec.caseId;
        el("fDate").value = rec.ym;
        el("fClerkId").value = rec.clerkId;
        el("fClerkName").value = rec.clerkName;
        el("fDept").value = rec.dept;
        el("fRegion").value = rec.region;
        el("fGroup").value = rec.group;
        el("fBranch").value = rec.branch + " " + rec.branchName;
        el("fVisitType").value = rec.visitType;
        el("fHasReport").value = rec.hasReport;
        el("fCloseStatus").value = rec.closeStatus;
        el("fPoints").value = rec.points;
        el("fPointsNote").value = rec.pointsNote || "";
        el("fProgressNote").value = rec.progressNote || "";
        el("fCaseContrib").value = rec.contrib;

        el("amount").value = rec.reportAmt;
        el("closedAmount").value = rec.closeAmt;
        setCheckedValues("#opportunities input", rec.bizType ? rec.bizType.split("、") : []);
        setCheckedValues(".unit input", rec.units ? rec.units.split("、") : []);

        revenue = rec.revenue || "成長";
        el("growth").value = rec.growth;
        el("shift").value = rec.shift || "三班";
        el("operation").value = rec.operation || "";
        el("risk").value = rec.risk || "";
        el("action").value = rec.action || "";
        el("due").value = rec.due || "2026-11-28";

        el("period").value = rec.ym;
        el("owner").value = rec.clerkId + " " + rec.clerkName + " (" + rec.branch + " " + rec.branchName + ")";
        el("reportDue").value = rec.due || "2026-11-28";
      }

      updateWeightPills();
      updateTickerAndAmounts();
      summary();
    }

    function updateWeightPills() {
      var hasRep = el("fHasReport").value;
      var closeSt = el("fCloseStatus").value;
      var w = calcStageWeight(hasRep, closeSt);
      el("stepVisit").className = "weight-step on";
      el("stepReport").className = "weight-step" + (hasRep === "有" ? " on" : "");
      el("stepClose").className = "weight-step" + (closeSt === "有" ? " on" : "");
      var pts = Number(el("fPoints").value || 0);
      el("totalWeightText").textContent = "階段權重：" + w.toFixed(1) + (pts > 0 ? " (另加專案點數 +" + pts + " 點)" : "");
    }

    function updateTickerAndAmounts() {
      var repVal = parseMoney(el("amount").value);
      var clsVal = parseMoney(el("closedAmount").value);
      el("oppValue").textContent = formatNT(repVal);
      el("closedValue").textContent = formatNT(clsVal);

      var filterMode = el("tickerFilter") ? el("tickerFilter").value : "PENDING";
      var items = [];
      for (var i = 0; i < table2Records.length; i++) {
        var r = table2Records[i];
        if (currentRole === "REGION" && r.region !== lockedRegion) continue;
        if (currentRole === "BRANCH" && r.branch !== lockedBranch) continue;

        var amt = parseMoney(r.reportAmt);
        if (filterMode === "PENDING") {
          if (r.closeStatus !== "有" && r.hasReport === "有") {
            items.push("🔥 【待督導追蹤案｜" + r.region + " " + r.branch + r.branchName + "】" + r.dept + "科 " + r.clerkName + " 爭攬【" + r.custShort + "】" + r.bizType + "（通報：" + r.reportAmt + "｜進度：" + r.progressNote + "）");
          }
        } else if (filterMode === "MAJOR") {
          if (amt >= 30000000 || r.points > 0) {
            items.push("💎 【" + r.region + " " + r.branch + r.branchName + "】" + r.custShort + " — " + r.bizType + " " + r.reportAmt + " (狀態:" + r.closeStatus + ")");
          }
        } else {
          items.push("📢 [" + r.branch + r.branchName + "] " + r.custShort + " " + r.bizType + " " + r.reportAmt + " (" + r.closeStatus + ")");
        }
        if (items.length >= 10) break; // 限制播報筆數確保跑馬燈清晰緩慢
      }
      if (!items.length) items.push("✅ 轄下目前無待督導之未結追蹤案件");
      el("tickerMessage").innerHTML = "📢 <b>權責戰情跑馬燈</b>　" + items.join("　　　｜　　　");
    }

    function summary() {
      var c = getCustomerById(currentCustId);
      var a = selected("#opportunities input");
      var u = selected(".unit input");
      var w = calcStageWeight(el("fHasReport").value, el("fCloseStatus").value);
      var t = [
        "【表一：客戶日結狀態】" + (c ? (c.shortName + "（" + c.fullName + "）｜歸屬：" + c.branch + c.branchName + "｜存款：" + c.deposit + "｜授信：" + c.loanBalance + "/" + c.loanLimit + "｜網銀GEB：" + c.geb) : ""),
        "【表二：爭攬案件資訊】案件 " + el("currentCaseBadge").textContent + "｜" + el("fBranch").value + " " + el("fDept").value + "科 行員 " + el("fClerkId").value + " " + el("fClerkName").value,
        "【商機與推動進度】通報：" + el("fHasReport").value + "（" + (a.length ? a.join("、") : "無") + " " + el("amount").value + "）｜成案狀態：" + el("fCloseStatus").value + "（成案：" + el("closedAmount").value + "）｜階段權重：" + w.toFixed(1),
        "【後續推動說明】" + el("fProgressNote").value,
        "【訪談重點與行動】" + el("operation").value + " ➔ 後續行動：" + el("action").value + "（期限：" + el("due").value + "）"
      ];
      el("visitSummary").textContent = t.join(NL);
      return t.join(NL);
    }

    function saveCurrentCaseToTable2() {
      var rec = getCaseById(currentCaseId);
      if (!rec) return;
      var bizTypes = selected("#opportunities input");
      var unitTypes = selected(".unit input");
      var hasRep = el("fHasReport").value;
      var closeSt = el("fCloseStatus").value;

      rec.ym = el("fDate").value.trim() || "2026-11";
      rec.clerkId = el("fClerkId").value.trim();
      rec.clerkName = el("fClerkName").value.trim();
      rec.dept = el("fDept").value;
      rec.visitType = el("fVisitType").value;
      rec.hasReport = hasRep;
      rec.bizType = hasRep === "無" ? "無" : (bizTypes.length ? bizTypes.join("、") : "授信");
      rec.reportAmt = hasRep === "無" ? "0" : el("amount").value.trim();
      rec.units = unitTypes.join("、");
      rec.closeStatus = closeSt;
      rec.progressNote = el("fProgressNote").value.trim();
      rec.closeAmt = closeSt === "有" ? el("closedAmount").value.trim() : "0";
      rec.points = Number(el("fPoints").value || 0);
      rec.pointsNote = el("fPointsNote").value.trim();
      rec.weight = calcStageWeight(hasRep, closeSt);
      rec.contrib = Number(el("fCaseContrib").value || 0);
      rec.operation = el("operation").value.trim();
      rec.risk = el("risk").value.trim();
      rec.action = el("action").value.trim();
      rec.due = el("due").value;

      renderSelectors();
      loadCurrentSelectionToUI();
      drawWarRoom();
      toast("✅ 已更新至表二《行員爭攬業務紀錄表》 (" + rec.caseId + ")");
    }

    function createNewCaseForCurrentCustomer() {
      var c = getCustomerById(currentCustId);
      if (!c) return;
      var nextNum = table2Records.length + 1;
      var newId = "CASE-202611-" + (nextNum < 100 ? "0" + nextNum : nextNum);
      var newRec = {
        caseId: newId, ym: "2026-11", date: "1151112",
        clerkId: c.rm || "1236", clerkName: "新增爭攬行員", dept: "營業",
        region: c.region, subRegion: c.subRegion, group: c.group, category: c.category,
        branch: c.branch, branchName: c.branchName, visitType: "約訪",
        custId: c.id, custShort: c.shortName, uni: c.uni, tier: c.tier,
        hasReport: "有", bizType: "授信", reportAmt: "3000萬", units: "授信單位、營業單位",
        closeStatus: "追蹤", progressNote: "新爭攬商機立案追蹤中", closeAmt: "0",
        points: 0, pointsNote: "", weight: 0.5, contrib: 120,
        revenue: "成長", growth: 15, shift: "三班",
        operation: "拜訪" + c.fullName + "，洽談新一波業務合作。",
        risk: "評估授信額度與企業網銀(GEB)需求。",
        action: "提交初步條件書並安排覆訪", due: "2026-11-30"
      };
      table2Records.unshift(newRec);
      currentCaseId = newId;
      renderSelectors();
      loadCurrentSelectionToUI();
      page("interview");
      toast("➕ 已為【" + c.shortName + "】新增爭攬紀錄 " + newId);
    }

    function makeReport() {
      var c = getCustomerById(currentCustId);
      var rec = getCaseById(currentCaseId);
      var types = selected("#opportunities input");
      var units = selected(".unit input");
      var owner = el("owner").value.trim();
      var due = el("reportDue").value || el("due").value;
      var source = el("source").value.trim();
      var period = el("period").value.trim();
      var w = calcStageWeight(el("fHasReport").value, el("fCloseStatus").value);

      var lines = [
        "【行銷拜訪暨業務爭攬推動報告】",
        "客戶代號／名稱：" + (c ? c.id + " " + c.shortName + " — " + el("cust").value : el("cust").value) + "（統編：" + el("uni").value + "）",
        "歸屬分行：" + (c ? c.region + " / " + c.group + " / " + c.branch + " " + c.branchName : "") + "｜產業別：" + el("industry").value + "｜報告月份：" + period,
        "資料來源：" + source,
        "",
        "一、客戶基本概況（表一：客戶每日狀態表）",
        "客戶名稱：" + el("cust").value + "。統一編號：" + el("uni").value + "。信評：" + el("rating").value + "。電話：" + el("custPhone").value + "。地址：" + el("custAddr").value + "。",
        "",
        "二、本行每日往來狀況（表一：日結餘額與網銀狀態）",
        "• 台幣存款餘額：" + (c ? c.deposit : "0") + "；外幣存款餘額：" + (c ? c.fxDeposit : "0") + "。",
        "• 授信往來狀況：動用餘額 " + (c ? c.loanBalance : "0") + " ／ 核准額度 " + (c ? c.loanLimit : "0") + "。",
        "• 理財基金狀況：基金餘額 " + (c ? c.fundBalance : "0") + "；本月新購 " + (c ? c.fundMonth : "0") + "。",
        "• 企業網銀 (GEB) 狀態：「" + (c ? c.geb : "") + "」；薪轉戶：「" + (c ? c.payroll : "") + "」；客戶貢獻度：" + (c ? c.contrib : 0) + " 點。",
        "",
        "三、本次訪談與業務爭攬推動情形（表二：" + (rec ? rec.caseId : "") + "）",
        "爭攬行員：" + el("fClerkId").value + " " + el("fClerkName").value + "（" + el("fBranch").value + " " + el("fDept").value + "科）。",
        "商機項目：" + (types.length ? types.join("、") : "無") + "；通報金額：" + el("amount").value + "；推動狀態：" + el("fCloseStatus").value + "；成案金額：" + el("closedAmount").value + "。",
        "推動進度說明：" + el("fProgressNote").value,
        "階段權重積分：" + w.toFixed(1) + " 分；專案點數：" + el("fPoints").value + " 點。",
        "訪談重點：" + el("operation").value,
        "風險與需求：" + el("risk").value,
        "",
        "四、後續行動與協作追蹤",
        "協作單位：" + (units.length ? units.join("、") : "待確認") + "。後續行動：" + el("action").value + "。負責人：" + owner + "。期限：" + due + "。"
      ];
      el("report").textContent = lines.join(NL);

      var checks = [
        ["表一客戶識別明確", !!el("cust").value && !!el("uni").value],
        ["拜訪期間明確", !!period],
        ["雙表來源揭露", !!source],
        ["表一每日往來與GEB呈現", !!c],
        ["表二爭攬行員明確", !!el("fClerkId").value],
        ["訪談重點呈現", !!el("operation").value],
        ["表二推動進度明確", !!el("fProgressNote").value],
        ["風險需求呈現", !!el("risk").value],
        ["負責人明確", !!owner],
        ["行動期限明確", !!due]
      ];
      var pass = 0, results = [];
      for (var i = 0; i < checks.length; i++) {
        if (checks[i][1]) pass++;
        results.push((checks[i][1] ? "✅ 符合" : "❌ 待補") + "：" + checks[i][0]);
      }
      var pct = Math.round((pass * 100) / checks.length);
      el("score").textContent = pct + "% " + (pct >= 85 ? "達門檻" : "未達85%");
      el("score").style.color = pct >= 85 ? "#16834a" : "#c5353d";
      el("checks").textContent = "檢核結果：" + pass + " / " + checks.length + " 項通過 — " + results.join("；");
      toast("📄 已產生完整雙表整合報告！");
    }

    function page(name) {
      var ps = document.querySelectorAll(".page");
      for (var i = 0; i < ps.length; i++) ps[i].classList.remove("active");
      el("page-" + name).classList.add("active");
      var as = document.querySelectorAll(".nav a");
      for (var j = 0; j < as.length; j++) {
        as[j].classList.toggle("active", as[j].getAttribute("data-page") === name);
      }
      if (name === "warroom") drawWarRoom();
      window.scrollTo(0, 0);
    }

    // 綁定事件
    el("rbacRole").addEventListener("change", applyRbacUIState);
    el("rbacRegionSelect").addEventListener("change", applyRbacUIState);
    el("rbacBranchSelect").addEventListener("change", applyRbacUIState);

    el("warMonthSelect").addEventListener("change", function() {
      var targetYm = this.value;
      var avail = getAvailableTimelineMonths();
      var idx = avail.indexOf(targetYm);
      if (idx !== -1) {
        lineMonthOffset = Math.max(0, Math.min(avail.length - MONTH_WINDOW, idx - MONTH_WINDOW + 1));
      }
      drawWarRoom();
    });
    el("warRegionFilter").addEventListener("change", function() {
      sliderOffsetT1 = 0;
      sliderOffsetT2 = 0;
      drawWarRoom();
    });
    el("warGroupFilter").addEventListener("change", function() {
      sliderOffsetT1 = 0;
      sliderOffsetT2 = 0;
      drawWarRoom();
    });
    el("warBranchSearch").addEventListener("input", function() {
      sliderOffsetT1 = 0;
      sliderOffsetT2 = 0;
      drawWarRoom();
    });
    el("insideBranchSelect").addEventListener("change", renderBranchInsidePanel);

    // 表一 & 表二 5家分行拉 BAR (Slider) 事件綁定
    el("sliderT1").addEventListener("input", function() {
      sliderOffsetT1 = Number(this.value || 0);
      if (el("syncSlidersChk") && el("syncSlidersChk").checked) {
        sliderOffsetT2 = sliderOffsetT1;
      }
      render5BranchBarCharts();
    });
    el("sliderT2").addEventListener("input", function() {
      sliderOffsetT2 = Number(this.value || 0);
      if (el("syncSlidersChk") && el("syncSlidersChk").checked) {
        sliderOffsetT1 = sliderOffsetT2;
      }
      render5BranchBarCharts();
    });
    el("syncSlidersChk").addEventListener("change", function() {
      if (this.checked) {
        sliderOffsetT2 = sliderOffsetT1;
        render5BranchBarCharts();
      }
    });

    el("btnT1Prev5").addEventListener("click", function() { stepSlider(1, -5); });
    el("btnT1Prev1").addEventListener("click", function() { stepSlider(1, -1); });
    el("btnT1Next1").addEventListener("click", function() { stepSlider(1, 1); });
    el("btnT1Next5").addEventListener("click", function() { stepSlider(1, 5); });

    el("btnT2Prev5").addEventListener("click", function() { stepSlider(2, -5); });
    el("btnT2Prev1").addEventListener("click", function() { stepSlider(2, -1); });
    el("btnT2Next1").addEventListener("click", function() { stepSlider(2, 1); });
    el("btnT2Next5").addEventListener("click", function() { stepSlider(2, 5); });

    // 表一 & 表二長條圖檢視層級切換 (5家分行拉BAR vs 5大業務分區總和 vs 5大組別總和)
    var scopePills = document.querySelectorAll("#topBarChartScopePills .metric-pill");
    for (var spIdx = 0; spIdx < scopePills.length; spIdx++) {
      scopePills[spIdx].addEventListener("click", function() {
        topBarChartScope = this.getAttribute("data-bscope");
        render5BranchBarCharts();
        if (topBarChartScope === "REGION_SUM") {
          lineBranchSource = "REGIONS_ALL";
          el("lineBranchSourceMode").value = "REGIONS_ALL";
          el("customBranchPickerToggleWrap").style.display = "none";
          renderMultiBranchCompareSection();
          toast("🗺️ 已切換為檢視【全行 4 大業務分區總和（北區／桃竹苗區／中區／南區）】對比");
        } else if (topBarChartScope === "GROUP_SUM") {
          lineBranchSource = "GROUPS_ALL";
          el("lineBranchSourceMode").value = "GROUPS_ALL";
          el("customBranchPickerToggleWrap").style.display = "none";
          renderMultiBranchCompareSection();
          toast("🏢 已切換為檢視【5 大規模組別總和】對比");
        } else {
          lineBranchSource = "SYNC_SLIDER";
          el("lineBranchSourceMode").value = "SYNC_SLIDER";
          el("customBranchPickerToggleWrap").style.display = "none";
          renderMultiBranchCompareSection();
          toast("🏦 已切換為檢視【轄下各分行排行 (每次5家+拉BAR)】");
        }
      });
    }

    el("btnQuickCompareRegions").addEventListener("click", function() {
      topBarChartScope = "REGION_SUM";
      lineBranchSource = "REGIONS_ALL";
      el("lineBranchSourceMode").value = "REGIONS_ALL";
      el("customBranchPickerToggleWrap").style.display = "none";
      render5BranchBarCharts();
      renderMultiBranchCompareSection();
      toast("📊 下方圖表已直接載入【全行 4 大業務分區總和】進行餘額柱狀圖與成長率折線比較！");
    });

    el("btnResetAllRegions").addEventListener("click", function() {
      el("warRegionFilter").value = "ALL";
      sliderOffsetT1 = 0;
      sliderOffsetT2 = 0;
      drawWarRoom();
      toast("🔄 已恢復檢視【全行 4 大業務分區（北區／桃竹苗區／中區／南區）】");
    });

    if (el("btnToggleHqRegCharts")) {
      el("btnToggleHqRegCharts").addEventListener("click", function() {
        var p = el("hqRegionsChartsPanel");
        if (!p) return;
        var isHidden = p.style.display === "none";
        p.style.display = isHidden ? "block" : "none";
        this.textContent = isHidden ? "🔼 收合各區發展圖表看板" : "📊 展開各區發展圖表看板";
      });
    }

    function stepHqRegMonthSlider(delta) {
      var availMonths = (hqRegModeKey === "MOM")
        ? allMonths.slice(1)
        : (hqRegModeKey === "YOY" ? allMonths.filter(function(ym) { return getYoYMonth(ym) !== null; }) : allMonths.slice());
      var maxMOff = Math.max(0, availMonths.length - MONTH_WINDOW);
      hqRegMonthOffset = Math.max(0, Math.min(maxMOff, hqRegMonthOffset + delta));
      renderHqRegionTotalsStrip();
    }

    if (el("hqRegBarMetricSelect")) {
      el("hqRegBarMetricSelect").addEventListener("change", function() {
        hqRegMetricKey = this.value;
        renderHqRegionTotalsStrip();
        syncZoomModalContent();
      });
    }
    if (el("hqRegLineMetricSelect")) {
      el("hqRegLineMetricSelect").addEventListener("change", function() {
        hqRegMetricKey = this.value;
        renderHqRegionTotalsStrip();
        syncZoomModalContent();
      });
    }
    if (el("hqRegModeSelect")) {
      el("hqRegModeSelect").addEventListener("change", function() {
        hqRegModeKey = this.value;
        var availMonths = (hqRegModeKey === "MOM")
          ? allMonths.slice(1)
          : (hqRegModeKey === "YOY" ? allMonths.filter(function(ym) { return getYoYMonth(ym) !== null; }) : allMonths.slice());
        var idx = availMonths.indexOf(selectedMonth);
        if (idx !== -1) {
          hqRegMonthOffset = Math.max(0, Math.min(availMonths.length - MONTH_WINDOW, idx - MONTH_WINDOW + 1));
        } else {
          hqRegMonthOffset = Math.max(0, availMonths.length - MONTH_WINDOW);
        }
        renderHqRegionTotalsStrip();
        syncZoomModalContent();
      });
    }
    if (el("sliderHqRegMonths")) {
      el("sliderHqRegMonths").addEventListener("input", function() {
        hqRegMonthOffset = Number(this.value || 0);
        renderHqRegionTotalsStrip();
      });
    }
    if (el("btnHqRegMonPrev6")) el("btnHqRegMonPrev6").addEventListener("click", function() { stepHqRegMonthSlider(-6); });
    if (el("btnHqRegMonPrev1")) el("btnHqRegMonPrev1").addEventListener("click", function() { stepHqRegMonthSlider(-1); });
    if (el("btnHqRegMonNext1")) el("btnHqRegMonNext1").addEventListener("click", function() { stepHqRegMonthSlider(1); });
    if (el("btnHqRegMonNext6")) el("btnHqRegMonNext6").addEventListener("click", function() { stepHqRegMonthSlider(6); });

    el("showComboBarsInTimeline").addEventListener("change", function() {
      renderMultiBranchCompareSection();
    });

    // 多分行 MoM / YoY 折線圖比較控制項事件綁定
    var mPills = document.querySelectorAll("#lineMetricPills .metric-pill");
    for (var mp = 0; mp < mPills.length; mp++) {
      mPills[mp].addEventListener("click", function() {
        for (var k = 0; k < mPills.length; k++) mPills[k].classList.remove("active");
        this.classList.add("active");
        lineMetricKey = this.getAttribute("data-metric");
        renderMultiBranchCompareSection();
      });
    }

    el("lineModeSelect").addEventListener("change", function() {
      lineModeKey = this.value;
      var avail = getAvailableTimelineMonths();
      var idx = avail.indexOf(selectedMonth);
      if (idx !== -1) {
        lineMonthOffset = Math.max(0, Math.min(avail.length - MONTH_WINDOW, idx - MONTH_WINDOW + 1));
      } else {
        lineMonthOffset = Math.max(0, avail.length - MONTH_WINDOW);
      }
      renderMultiBranchCompareSection();
    });

    el("lineBranchSourceMode").addEventListener("change", function() {
      lineBranchSource = this.value;
      el("customBranchPickerToggleWrap").style.display = lineBranchSource === "CUSTOM" ? "block" : "none";
      if (lineBranchSource === "CUSTOM") {
        // 若尚未自訂或為空，預設帶入目前拉 BAR 的 5 家
        var cur5 = cachedSortedBranches.slice(sliderOffsetT1, sliderOffsetT1 + BAR_WINDOW).map(function(b) { return b.code; });
        if (cur5.length) customPickedCodes = cur5;
        renderCustomBranchChips();
      }
      renderMultiBranchCompareSection();
    });

    el("customBranchSearchInput").addEventListener("input", renderCustomBranchChips);

    el("sliderCompare").addEventListener("input", function() {
      compareSliderOffset = Number(this.value || 0);
      renderMultiBranchCompareSection();
    });
    el("btnCmpPrev5").addEventListener("click", function() { stepCompareSlider(-5); });
    el("btnCmpPrev1").addEventListener("click", function() { stepCompareSlider(-1); });
    el("btnCmpNext1").addEventListener("click", function() { stepCompareSlider(1); });
    el("btnCmpNext5").addEventListener("click", function() { stepCompareSlider(5); });

    el("sliderLineMonths").addEventListener("input", function() {
      lineMonthOffset = Number(this.value || 0);
      renderMultiBranchCompareSection();
    });
    el("btnMonPrev6").addEventListener("click", function() { stepLineMonthSlider(-6); });
    el("btnMonPrev1").addEventListener("click", function() { stepLineMonthSlider(-1); });
    el("btnMonNext1").addEventListener("click", function() { stepLineMonthSlider(1); });
    el("btnMonNext6").addEventListener("click", function() { stepLineMonthSlider(6); });

    el("btnPickTop5").addEventListener("click", function() {
      customPickedCodes = cachedSortedBranches.slice(0, 5).map(function(b) { return b.code; });
      compareSliderOffset = 0;
      renderCustomBranchChips();
      renderMultiBranchCompareSection();
    });

    el("btnPickTop10").addEventListener("click", function() {
      customPickedCodes = cachedSortedBranches.slice(0, 10).map(function(b) { return b.code; });
      compareSliderOffset = 0;
      renderCustomBranchChips();
      renderMultiBranchCompareSection();
      toast("✅ 已勾選前 10 名分行，圖表窗格維持顯示 5 家，可由下方拉 BAR 拖曳檢視！");
    });

    el("btnPickAllAllowed").addEventListener("click", function() {
      customPickedCodes = cachedSortedBranches.map(function(b) { return b.code; });
      compareSliderOffset = 0;
      renderCustomBranchChips();
      renderMultiBranchCompareSection();
      toast("✅ 已全選轄下 " + customPickedCodes.length + " 家分行，圖表窗格維持 5 家，可由下方拉 BAR 拖曳檢視！");
    });

    el("btnPickSlider5").addEventListener("click", function() {
      customPickedCodes = cachedSortedBranches.slice(sliderOffsetT1, sliderOffsetT1 + BAR_WINDOW).map(function(b) { return b.code; });
      compareSliderOffset = 0;
      renderCustomBranchChips();
      renderMultiBranchCompareSection();
    });

    el("btnClearPicked").addEventListener("click", function() {
      if (cachedSortedBranches.length) {
        customPickedCodes = [cachedSortedBranches[0].code];
      }
      compareSliderOffset = 0;
      renderCustomBranchChips();
      renderMultiBranchCompareSection();
      toast("已重置為第 1 名分行，請點選下方分行標籤加入比較");
    });

    var wTabs = document.querySelectorAll("#warSubTabs .sub-tab");
    for (var wt = 0; wt < wTabs.length; wt++) {
      wTabs[wt].addEventListener("click", function() {
        switchWarSubTab(this.getAttribute("data-wtab"));
      });
    }

    el("tickerFilter").addEventListener("change", updateTickerAndAmounts);
    el("tickerSpeed").addEventListener("change", function() {
      el("tickerMessage").style.animationDuration = this.value;
    });
    el("tickerPauseBtn").addEventListener("click", function() {
      var isPaused = el("tickerMessage").classList.toggle("paused");
      this.textContent = isPaused ? "▶️ 播放" : "⏸️ 暫停";
    });

    el("customerSelect").addEventListener("change", function() {
      currentCustId = this.value;
      renderCaseSelectorForCustomer(currentCustId);
      loadCurrentSelectionToUI();
    });
    el("caseSelect").addEventListener("change", function() {
      currentCaseId = this.value;
      loadCurrentSelectionToUI();
    });
    el("newCaseBtn").addEventListener("click", createNewCaseForCurrentCustomer);
    el("saveToTable2Btn").addEventListener("click", saveCurrentCaseToTable2);
    el("fHasReport").addEventListener("change", updateWeightPills);
    el("fCloseStatus").addEventListener("change", updateWeightPills);
    el("fPoints").addEventListener("input", updateWeightPills);

    var navLinks = document.querySelectorAll(".nav a");
    for (var n = 0; n < navLinks.length; n++) {
      navLinks[n].addEventListener("click", function(e) {
        e.preventDefault();
        page(this.getAttribute("data-page"));
      });
    }

    el("amount").addEventListener("input", updateTickerAndAmounts);
    el("closedAmount").addEventListener("input", updateTickerAndAmounts);
    el("summaryBtn").addEventListener("click", function() { summary(); toast("摘要預覽已更新"); });
    el("makeReport").addEventListener("click", makeReport);
    el("print").addEventListener("click", function() { window.print(); });
    el("guardianBtn").addEventListener("click", function() {
      var s = el("sources");
      s.style.display = s.style.display === "none" ? "block" : "none";
    });

    // =========================================================================
    // 圖表放大檢視互動視窗 (Chart Zoom Modal) 控制邏輯
    // =========================================================================
    function getChartMetaForZoom(chartId) {
      if (chartId === "chartBranchBalances") {
        return {
          title: el("chart1Title") ? el("chart1Title").textContent : "🏦 表一：各分行存款／授信／基金餘額對比",
          hasSlider: topBarChartScope === "BRANCH_5",
          sliderLabel: "↔️ 拉 BAR 檢視其他分行（維持 5 家）：",
          min: 0,
          max: el("sliderT1") ? Number(el("sliderT1").max || 0) : 0,
          val: sliderOffsetT1,
          badge: el("sliderT1RangeText") ? el("sliderT1RangeText").textContent : "",
          stepBig: 5
        };
      } else if (chartId === "chartBranchConversion") {
        return {
          title: el("chart2Title") ? el("chart2Title").textContent : "🚀 表二：各分行通報商機 vs 實際成案金額對比",
          hasSlider: topBarChartScope === "BRANCH_5",
          sliderLabel: "↔️ 拉 BAR 檢視其他分行（維持 5 家）：",
          min: 0,
          max: el("sliderT2") ? Number(el("sliderT2").max || 0) : 0,
          val: sliderOffsetT2,
          badge: el("sliderT2RangeText") ? el("sliderT2RangeText").textContent : "",
          stepBig: 5
        };
      } else if (chartId === "chartMultiBranchBar") {
        return {
          title: el("comboBarChartTitle") ? el("comboBarChartTitle").textContent : "📊 對應業務【餘額／實績柱狀圖（去年同月／上月／當月對比）】",
          hasSlider: true,
          sliderLabel: "↔️ 分行拉 BAR（窗格維持 5 家）：",
          min: 0,
          max: el("sliderCompare") ? Number(el("sliderCompare").max || 0) : 0,
          val: compareSliderOffset,
          badge: el("compareSliderRangeText") ? el("compareSliderRangeText").textContent : "",
          stepBig: 5
        };
      } else if (chartId === "chartMultiBranchLine") {
        return {
          title: el("comboLineChartTitle") ? el("comboLineChartTitle").textContent : "📈 對應業務【逐月成長率折線圖 ＋ 各月餘額柱狀圖（每次顯示 6 個月）】",
          hasSlider: true,
          sliderLabel: "📅 月份拉 BAR（窗格維持 6 個月）：",
          min: 0,
          max: el("sliderLineMonths") ? Number(el("sliderLineMonths").max || 0) : 0,
          val: lineMonthOffset,
          badge: el("monthSliderRangeText") ? el("monthSliderRangeText").textContent : "",
          stepBig: 6
        };
      } else if (chartId === "chartHqRegBar") {
        return {
          title: "🏛️ 全行 4 大分區（北區／桃竹苗區／中區／南區）餘額／實績柱狀圖（去年同月／上月／當月對比）",
          hasSlider: false,
          sliderLabel: "",
          min: 0,
          max: 0,
          val: 0,
          badge: "全行 4 大分區對比",
          stepBig: 5
        };
      } else if (chartId === "chartHqRegLine") {
        return {
          title: "📈 全行 4 大分區（北區／桃竹苗區／中區／南區）逐月成長率折線 ＋ 各月餘額柱狀圖",
          hasSlider: true,
          sliderLabel: "📅 各區月份拉 BAR（窗格維持 6 個月）：",
          min: 0,
          max: el("sliderHqRegMonths") ? Number(el("sliderHqRegMonths").max || 0) : 0,
          val: hqRegMonthOffset,
          badge: el("hqRegMonthRangeText") ? el("hqRegMonthRangeText").textContent : "",
          stepBig: 6
        };
      }
      var box = el(chartId);
      var cardTitle = "📊 圖表放大檢視";
      if (box && box.parentElement) {
        var bNode = box.parentElement.querySelector("b");
        if (bNode) cardTitle = bNode.textContent;
      }
      return {
        title: cardTitle,
        hasSlider: false,
        sliderLabel: "",
        min: 0,
        max: 0,
        val: 0,
        badge: "全幅高解析度檢視",
        stepBig: 5
      };
    }

    function applyZoomScaleToStage() {
      var stage = el("zoomModalStage");
      if (!stage) return;
      var svgEl = stage.querySelector("svg");
      if (svgEl) {
        var baseH = Math.round(390 * zoomScaleFactor);
        var baseW = Math.round(100 * zoomScaleFactor);
        svgEl.style.setProperty("height", baseH + "px", "important");
        svgEl.style.setProperty("width", baseW + "%", "important");
        svgEl.style.setProperty("margin", "0 auto", "important");
        svgEl.style.setProperty("display", "block", "important");
      }
    }

    function syncZoomModalContent() {
      if (!activeZoomChartId) return;
      var srcBox = el(activeZoomChartId);
      var stage = el("zoomModalStage");
      if (!srcBox || !stage) return;

      var meta = getChartMetaForZoom(activeZoomChartId);
      var isMultiMetricChart = (
        activeZoomChartId === "chartMultiBranchBar" ||
        activeZoomChartId === "chartMultiBranchLine" ||
        activeZoomChartId === "chartHqRegBar" ||
        activeZoomChartId === "chartHqRegLine"
      );
      var isHqRegChart = (activeZoomChartId === "chartHqRegBar" || activeZoomChartId === "chartHqRegLine");
      var zMetricSel = el("zoomMetricSelect");
      var zModeSel = el("zoomModeSelect");
      if (zMetricSel && zModeSel) {
        zMetricSel.style.display = isMultiMetricChart ? "inline-block" : "none";
        zModeSel.style.display = (activeZoomChartId === "chartMultiBranchLine" || activeZoomChartId === "chartHqRegLine") ? "inline-block" : "none";
        zMetricSel.value = isHqRegChart ? hqRegMetricKey : lineMetricKey;
        zModeSel.value = isHqRegChart ? hqRegModeKey : lineModeKey;
      }
      if (activeZoomChartId === "chartMultiBranchLine" || activeZoomChartId === "chartHqRegLine") {
        el("zoomModalTitle").textContent = "";
      } else {
        el("zoomModalTitle").textContent = meta.title;
      }

      // 複製圖表內容並移除右下角小放大按鈕
      stage.innerHTML = srcBox.innerHTML;
      var floatBtn = stage.querySelector(".chart-zoom-float");
      if (floatBtn) floatBtn.remove();
      applyZoomScaleToStage();

      var ctrlWrap = el("zoomModalSliderControls");
      var rangeInput = el("zoomModalRangeInput");
      if (ctrlWrap && rangeInput) {
        ctrlWrap.style.display = meta.hasSlider ? "flex" : "none";
        el("zoomModalSliderLabel").textContent = meta.sliderLabel;
        rangeInput.min = String(meta.min);
        rangeInput.max = String(meta.max);
        rangeInput.value = String(meta.val);
        rangeInput.disabled = meta.max <= 0;
        el("zoomModalRangeBadge").textContent = meta.badge;
        el("btnZoomStepPrevBig").textContent = "⏮ -" + meta.stepBig;
        el("btnZoomStepNextBig").textContent = "+" + meta.stepBig + " ⏭";
      }
    }

    el("inlineBarMetricSelect").addEventListener("change", function() {
      lineMetricKey = this.value;
      renderMultiBranchCompareSection();
      syncZoomModalContent();
    });
    el("inlineLineMetricSelect").addEventListener("change", function() {
      lineMetricKey = this.value;
      renderMultiBranchCompareSection();
      syncZoomModalContent();
    });
    el("zoomMetricSelect").addEventListener("change", function() {
      if (activeZoomChartId === "chartHqRegBar" || activeZoomChartId === "chartHqRegLine") {
        hqRegMetricKey = this.value;
        renderHqRegionTotalsStrip();
      } else {
        lineMetricKey = this.value;
        renderMultiBranchCompareSection();
      }
      syncZoomModalContent();
    });
    el("zoomModeSelect").addEventListener("change", function() {
      if (activeZoomChartId === "chartHqRegLine") {
        hqRegModeKey = this.value;
        var availM = (hqRegModeKey === "MOM")
          ? allMonths.slice(1)
          : (hqRegModeKey === "YOY" ? allMonths.filter(function(ym) { return getYoYMonth(ym) !== null; }) : allMonths.slice());
        var idxM = availM.indexOf(selectedMonth);
        if (idxM !== -1) {
          hqRegMonthOffset = Math.max(0, Math.min(availM.length - MONTH_WINDOW, idxM - MONTH_WINDOW + 1));
        } else {
          hqRegMonthOffset = Math.max(0, availM.length - MONTH_WINDOW);
        }
        renderHqRegionTotalsStrip();
      } else {
        lineModeKey = this.value;
        var avail = getAvailableTimelineMonths();
        var idx = avail.indexOf(selectedMonth);
        if (idx !== -1) {
          lineMonthOffset = Math.max(0, Math.min(avail.length - MONTH_WINDOW, idx - MONTH_WINDOW + 1));
        } else {
          lineMonthOffset = Math.max(0, avail.length - MONTH_WINDOW);
        }
        renderMultiBranchCompareSection();
      }
      syncZoomModalContent();
    });

    function openChartZoomModal(chartId) {
      activeZoomChartId = chartId;
      zoomScaleFactor = 1;
      syncZoomModalContent();
      var modal = el("chartZoomModal");
      if (modal) modal.style.display = "flex";
    }

    function closeChartZoomModal() {
      activeZoomChartId = null;
      var modal = el("chartZoomModal");
      if (modal) modal.style.display = "none";
    }

    function stepActiveZoomSlider(delta) {
      if (!activeZoomChartId) return;
      if (activeZoomChartId === "chartBranchBalances") {
        stepSlider(1, delta);
      } else if (activeZoomChartId === "chartBranchConversion") {
        stepSlider(2, delta);
      } else if (activeZoomChartId === "chartMultiBranchBar") {
        if (lineBranchSource !== "CUSTOM") {
          stepSlider(1, delta);
        } else {
          stepCompareSlider(delta);
        }
      } else if (activeZoomChartId === "chartMultiBranchLine") {
        stepLineMonthSlider(delta);
      } else if (activeZoomChartId === "chartHqRegLine") {
        stepHqRegMonthSlider(delta);
      }
      syncZoomModalContent();
    }

    document.addEventListener("click", function(e) {
      var btn = e.target.closest ? e.target.closest("[data-zoom-chart]") : null;
      if (btn) {
        e.preventDefault();
        openChartZoomModal(btn.getAttribute("data-zoom-chart"));
      }
    });

    el("btnCloseZoomModal").addEventListener("click", closeChartZoomModal);
    el("chartZoomModal").addEventListener("click", function(e) {
      if (e.target === this) closeChartZoomModal();
    });
    document.addEventListener("keydown", function(e) {
      if (e.key === "Escape" && activeZoomChartId) closeChartZoomModal();
    });

    var zoomScaleBtns = document.querySelectorAll("[data-zoom-scale]");
    for (var zs = 0; zs < zoomScaleBtns.length; zs++) {
      zoomScaleBtns[zs].addEventListener("click", function() {
        zoomScaleFactor = Number(this.getAttribute("data-zoom-scale") || 1);
        applyZoomScaleToStage();
      });
    }

    el("zoomModalRangeInput").addEventListener("input", function() {
      var v = Number(this.value || 0);
      if (activeZoomChartId === "chartBranchBalances") {
        sliderOffsetT1 = v;
        if (el("syncSlidersChk") && el("syncSlidersChk").checked) sliderOffsetT2 = v;
        render5BranchBarCharts();
      } else if (activeZoomChartId === "chartBranchConversion") {
        sliderOffsetT2 = v;
        if (el("syncSlidersChk") && el("syncSlidersChk").checked) sliderOffsetT1 = v;
        render5BranchBarCharts();
      } else if (activeZoomChartId === "chartMultiBranchBar") {
        if (lineBranchSource !== "CUSTOM") {
          sliderOffsetT1 = v;
          if (el("syncSlidersChk") && el("syncSlidersChk").checked) sliderOffsetT2 = v;
          render5BranchBarCharts();
        } else {
          compareSliderOffset = v;
          renderMultiBranchCompareSection();
        }
      } else if (activeZoomChartId === "chartMultiBranchLine") {
        lineMonthOffset = v;
        renderMultiBranchCompareSection();
      } else if (activeZoomChartId === "chartHqRegLine") {
        hqRegMonthOffset = v;
        renderHqRegionTotalsStrip();
      }
      syncZoomModalContent();
    });

    el("btnZoomStepPrevBig").addEventListener("click", function() {
      var meta = getChartMetaForZoom(activeZoomChartId);
      stepActiveZoomSlider(-meta.stepBig);
    });
    el("btnZoomStepPrev1").addEventListener("click", function() { stepActiveZoomSlider(-1); });
    el("btnZoomStepNext1").addEventListener("click", function() { stepActiveZoomSlider(1); });
    el("btnZoomStepNextBig").addEventListener("click", function() {
      var meta = getChartMetaForZoom(activeZoomChartId);
      stepActiveZoomSlider(meta.stepBig);
    });

    // 啟動初始化
    el("clock").textContent = new Date().toLocaleString("zh-TW", { hour12: false });
    initStaticDropdowns();
    applyRbacUIState();
  })();
  </script>
</body>
</html>
"""

final_html = HTML_TEMPLATE.replace("__SIM_PAYLOAD__", payload_json_str)

with open("BusinessWarRoom.html", "w", encoding="utf-8") as f:
    f.write(final_html)

with open(r"C:\Users\User\.gemini\antigravity\brain\e1f51b9f-b6e8-474b-a608-52b3b50cbad5\BusinessWarRoom_Preview.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Successfully built BusinessWarRoom.html and synced BusinessWarRoom_Preview.html, size:", len(final_html))
