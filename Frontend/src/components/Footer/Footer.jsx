
import styles from './Footer.module.css';
import white_logo from '../../images/white_logo.svg';

function Footer() {
  return (
    <footer className={styles.footer}>
      <div className="footer-content">
        <div className={styles.footerLeft}>
          <img src={white_logo} alt="Logo" className={styles.whiteLogo} />
          <div>+7-8352-20-12-09, Telegram</div>
        </div>
        <div className={styles.footerRight}>
          © Мой Силант 2022
        </div>
      </div>
    </footer>
  );
}

export default Footer;