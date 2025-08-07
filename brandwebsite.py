# 导入必要的库
import streamlit as st  # Streamlit 核心库，用于构建网页应用
import base64  # 用于编码/解码数据，这里用于处理图片
from PIL import Image  # Python图像处理库
import io  # 用于处理输入输出流
import os  # 用于处理文件路径

# 设置页面配置
st.set_page_config(
    page_title="—— | ——",  # 浏览器标签页标题
    page_icon="🚀",  # 浏览器标签页图标(可以使用emoji)
    layout="wide",  # 使用宽屏布局
    initial_sidebar_state="collapsed"  # 初始状态下折叠侧边栏
)

# 自定义CSS样式函数
def local_css(file_name):
    """从本地文件加载CSS样式"""
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==================== 页面结构开始 ====================

# 使用st.markdown创建导航栏，unsafe_allow_html=True允许使用原始HTML
st.markdown("""
<nav class="navbar">
    <div class="navbar-container">
        <a href="#" class="logo">企业名称</a>  <!-- 品牌logo -->
        <div class="nav-links">
            <a href="#home">首页</a>  <!-- 导航链接，使用锚点跳转 -->
            <a href="#about">关于我们</a>
            <a href="#services">服务</a>
            <a href="#portfolio">案例</a>
            <a href="#team">团队</a>
            <a href="#contact">联系我们</a>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

# 首屏展示区(Hero Section)
st.markdown("""
<div class="hero" id="home"><!-- id用于导航定位 -->
    <div class="hero-content">
        <h1>创新科技解决方案</h1>  <!-- 主标题 -->
        <p>为企业提供前沿的数字化转型服务，助力业务增长</p>  <!-- 副标题 -->
        <a href="#services" class="btn">探索我们的服务</a>  <!-- 行动按钮 -->
    </div>
</div>
""", unsafe_allow_html=True)

# 关于我们部分
st.markdown("""
<div class="section" id="about">  <!-- 区块id -->
    <div class="container">  <!-- 内容容器，控制最大宽度 -->
        <div class="section-header">  <!-- 区块标题区域 -->
            <h2>关于 ”企业名称“</h2>
            <p>引领创新，创造价值</p>
        </div>
        
<div class="about-content">  <!-- 关于内容 -->
               <h2> 我们的故事<h2>
                <p><p>
    <div class="about-text">
    <h3>我们的使命</h3> <!-- 小标题 -->
    <p></p>
</div>
                
""", unsafe_allow_html=True)
#logo = Image.open()  # 加载本地图片
#st.image(logo, caption="公司Logo", width=200)  # 显示图片，设置宽度为100像素

# 服务展示部分
st.markdown("""
<div class="section services" id="services">
<div class="container">
    <div class="section-header">
    <h2>我们的服务</h2>
     <p>专业定制解决方案</p>
</div>
        
<div class="services-grid">
    <div class="service-card">
        <div class="service-icon">💻</div>  <!-- 使用emoji作为图标 -->
        <h3>企业软件开发</h3>
        <p>定制化企业级应用开发，提高运营效率</p>
</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 案例展示部分
st.markdown("""
<div class="section portfolio" id="portfolio">
<div class="container">
    <div class="section-header">
        <h2>成功案例</h2>
        <p>见证我们的专业实力</p>
</div>
        
<div class="portfolio-grid">
    <div class="portfolio-item">
        <div class="portfolio-image" style="background-color: #4e89ae;"></div>
        <div class="portfolio-content">
            <h3>全球零售企业数字化转型</h3>
            <p></p>
</div>
            </div>
            <!-- 其他案例项目... -->
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 团队介绍部分
st.markdown("""
<div class="section team" id="team">
    <div class="container">
        <div class="section-header">
            <h2>专业团队</h2>
            <p>汇聚行业顶尖人才</p>
        </div>
        
<div class="team-grid">
    <div class="team-member">
        <div class="member-photo" style="background-color: #68b0ab;"></div>
        <h3>张明</h3>
        <p>创始人 & CEO</p>
        <div class="social-links">
            <a href="#">LinkedIn</a> | <a href="#">Twitter</a>
        </div>
    </div>
            <!-- 其他团队成员... -->
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 联系表单部分
st.markdown("""
<div class="section contact" id="contact">
    <div class="container">
        <div class="section-header">
            <h2>联系我们</h2>
            <p>随时为您提供咨询服务</p>
        </div>
        
<div class="contact-container">  <!-- 两栏布局 -->
    <div class="contact-info">  <!-- 左侧联系信息 -->
        <h3>联系方式</h3>
        <p><strong>地址:</strong> </p>
        <!-- 其他联系信息... -->
        
<div class="map-placeholder">
            <p>地图位置</p>  <!-- 地图占位符 -->
        </div>
            </div>
            
<div class="contact-form">  <!-- 右侧联系表单 -->
                <h3>发送消息</h3>
                <form>
                    <div class="form-group">
                        <input type="text" placeholder="您的姓名" required>
                    </div>
                    <!-- 其他表单字段... -->
                    <button type="submit" class="btn">发送消息</button>
                </form>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 页脚部分
st.markdown("""
<footer>
<div class="container">
        <div class="footer-content">  <!-- 三栏布局 -->
            <div class="footer-logo">
                <h3>TechVision</h3>
                <p>创新科技解决方案提供商</p>
            </div>
            
<div class="footer-links">
                <h4>快速链接</h4>
                <ul>
                    <li><a href="#home">首页</a></li>
                    <!-- 其他链接... -->
                </ul>
            </div>
            
<div class="footer-newsletter">
                <h4>订阅我们的通讯</h4>
                <form>
                    <input type="email" placeholder="您的邮箱地址">
                    <button type="submit">订阅</button>
                </form>
            </div>
        </div>
        
<div class="footer-bottom">  <!-- 底部版权和社交链接 -->
            <p>&copy; 2025 大学腾飞营. 保留所有权利</p>
            <div class="social-icons">
                <a href="#">微信</a>
                <!-- 其他社交链接... -->
            </div>
        </div>
    </div>
</footer>
""", unsafe_allow_html=True)

# ==================== CSS样式部分 ====================
primary_color = st.sidebar.color_picker ("选择主品牌色", "#2563eb")  # 侧边栏颜色选择器
primary_dark = st.sidebar.color_picker("深色主品牌色", "#1d4ed8")
secondary_color = st.sidebar.color_picker("次要文本色", "#64748b")
light_color = st.sidebar.color_picker("浅背景色", "#f8fafc")
dark_color = st.sidebar.color_picker("深文本色", "#0f0f2a")
accent_color = st.sidebar.color_picker("强调色", "#f59e0b")



# 注入自定义CSS样式
st.markdown(f"""
<style>
:root {{
    --primary: {primary_color};
    --primary-dark: {primary_dark};
    --secondary: {secondary_color};
    --light: {light_color};
    --dark: {dark_color};
    --accent: {accent_color};
}}

/* 页面全局样式 */
* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}}

body {{
    background-color: var(--light);
    color: var(--dark);
    line-height: 1.6;
}}

/* 导航栏样式 */
.navbar {{
    background-color: white;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
    padding: 1rem 0;
}}

.navbar-container {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}}

.logo {{
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--primary);
    text-decoration: none;
}}

.nav-links {{
    display: flex;
    gap: 2rem;
}}

.nav-links a {{
    color: var(--dark);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s;
}}

.nav-links a:hover {{
    color: var(--primary);
}}

/* 首屏区域样式 */
.hero {{
    height: 80vh;
    background: linear-gradient(135deg, var(--primary-dark) 0%, var(--primary) 100%);
    color: white;
    display: flex;
    align-items: center;
    padding-top: 60px;
}}

.hero-content {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    width: 100%;
}}

.hero-content h1 {{
    font-size: 3rem;
    margin-bottom: 1.5rem;
    line-height: 1.2;
}}

.hero-content p {{
    font-size: 1.3rem;
    margin-bottom: 2rem;
    max-width: 600px;
}}

.btn {{
    display: inline-block;
    background-color: var(--accent);
    color: var(--dark);
    padding: 0.8rem 2rem;
    border-radius: 4px;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
}}

.btn:hover {{
    background-color: #e69008;
    transform: translateY(-3px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}}

/* 内容区块样式 */
.section {{
    padding: 5rem 0;
}}

.container {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}}

.section-header {{
    text-align: center;
    margin-bottom: 4rem;
}}

.section-header h2 {{
    font-size: 2.5rem;
    color: var(--dark);
    margin-bottom: 1rem;
}}

.section-header p {{
    color: var(--secondary);
    font-size: 1.2rem;
    max-width: 700px;
    margin: 0 auto;
}}

/* 服务卡片样式 */
.services-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}}

.service-card {{
    background-color: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    text-align: center;
    transition: all 0.3s ease;
}}

.service-card:hover {{
    transform: translateY(-10px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
}}

.service-icon {{
    font-size: 3rem;
    margin-bottom: 1.5rem;
    color: var(--primary);
}}

.service-card h3 {{
    margin-bottom: 1rem;
    color: var(--dark);
}}

/* 页脚样式 */
.footer {{
    background-color: var(--dark);
    color: #cbd5e1;
    padding: 4rem 0 2rem;
}}

.footer-content {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 3rem;
    margin-bottom: 3rem;
}}

.footer-logo h3 {{
    color: white;
    font-size: 1.8rem;
    margin-bottom: 1rem;
}}

.footer-links h4,
.footer-newsletter h4 {{
    color: white;
    margin-bottom: 1.5rem;
    font-size: 1.2rem;
}}

.footer-links ul {{
    list-style: none;
}}

.footer-links li {{
    margin-bottom: 0.8rem;
}}

.footer-links a {{
    color: #94a3b8;
    text-decoration: none;
    transition: color 0.3s;
}}

.footer-links a:hover {{
    color: white;
}}

.footer-newsletter input {{
    width: 100%;
    padding: 0.8rem;
    border: none;
    border-radius: 4px;
    margin-bottom: 1rem;
}}

.footer-newsletter button {{
    background-color: var(--primary);
    color: white;
    border: none;
    padding: 0.8rem 1.5rem;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 500;
}}

.footer-bottom {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 2rem;
    border-top: 1px solid #334155;
}}

.social-icons a {{
    color: #94a3b8;
    margin-left: 1.5rem;
    text-decoration: none;
    transition: color 0.3s;
}}

.social-icons a:hover {{
    color: white;
}}

/* 响应式设计 */
@media (max-width: 768px) {{
    .nav-links {{
        display: none;
    }}
    
    .hero-content h1 {{
        font-size: 2.5rem;
    }}
}}
</style>
""", unsafe_allow_html=True)