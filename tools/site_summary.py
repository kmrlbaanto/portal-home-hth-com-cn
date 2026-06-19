import json
from datetime import datetime


def load_site_data():
    """
    加载内置站点资料数据。
    返回一个列表，每个元素为包含站点信息的字典。
    """
    return [
        {
            "url": "https://portal-home-hth.com.cn",
            "keywords": ["华体会", "体育", "娱乐", "在线服务"],
            "tags": ["门户", "综合平台", "中文"],
            "description": "华体会官方门户，提供体育、娱乐等多元化在线服务。"
        },
        {
            "url": "https://portal-home-hth.com.cn/news",
            "keywords": ["华体会", "资讯", "动态", "新闻"],
            "tags": ["资讯", "新闻中心"],
            "description": "华体会平台的最新资讯与动态发布页面。"
        },
        {
            "url": "https://portal-home-hth.com.cn/about",
            "keywords": ["华体会", "公司", "简介", "团队"],
            "tags": ["关于我们", "品牌介绍"],
            "description": "了解华体会平台的背景、团队与企业文化。"
        }
    ]


def collect_keywords(data_list):
    """从站点数据中收集所有关键词，去重后返回。"""
    all_keywords = set()
    for item in data_list:
        for kw in item.get("keywords", []):
            all_keywords.add(kw)
    return sorted(all_keywords)


def collect_tags(data_list):
    """从站点数据中收集所有标签，去重后返回。"""
    all_tags = set()
    for item in data_list:
        for tag in item.get("tags", []):
            all_tags.add(tag)
    return sorted(all_tags)


def generate_summary(data_list):
    """
    生成一份结构化的摘要文本。
    包括站点总数、关键词、标签、各站点详情等。
    """
    lines = []
    lines.append("=" * 60)
    lines.append("站点资料结构化摘要")
    lines.append("生成时间: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    lines.append("=" * 60)
    lines.append("")

    # 统计信息
    lines.append(f"站点总数: {len(data_list)}")
    lines.append("")

    # 关键词
    keywords = collect_keywords(data_list)
    lines.append(f"核心关键词 ({len(keywords)}):")
    for kw in keywords:
        lines.append(f"  - {kw}")
    lines.append("")

    # 标签
    tags = collect_tags(data_list)
    lines.append(f"标签集合 ({len(tags)}):")
    for tag in tags:
        lines.append(f"  - {tag}")
    lines.append("")

    # 各站点详情
    lines.append("站点详情:")
    for idx, site in enumerate(data_list, 1):
        lines.append(f"  [{idx}]")
        lines.append(f"      URL: {site.get('url', 'N/A')}")
        lines.append(f"      关键词: {', '.join(site.get('keywords', []))}")
        lines.append(f"      标签: {', '.join(site.get('tags', []))}")
        lines.append(f"      说明: {site.get('description', 'N/A')}")
        lines.append("")

    # 末尾装饰
    lines.append("=" * 60)
    lines.append("摘要结束")
    lines.append("=" * 60)
    return "\n".join(lines)


def save_summary_to_file(content, filename="site_summary_output.txt"):
    """将摘要内容写入文件。"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"摘要已保存至: {filename}")


def main():
    """
    主函数：加载数据、生成摘要、保存并打印摘要。
    """
    data = load_site_data()
    summary_text = generate_summary(data)
    print(summary_text)
    save_summary_to_file(summary_text)


if __name__ == "__main__":
    main()