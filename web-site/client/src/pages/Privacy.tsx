import React from "react";

import "./guild/styles.css";
import { Footer } from "../components/Footer";
import { NavBar } from "../components/NavBar";

export const Privacy: React.FC = () => {
  document.title = `XGN BOT - Privacy`;
  return (
    <div>
      <NavBar />
      <div
        style={{ background: "var(--background)" }}
        className="features-boxed"
      >
        <div className="container">
          <br />
          <br />
          <div className="card" style={{ background: "#2c2f33" }}>
            <div className="card-body">
              <h1
                className="d-xl-flex justify-content-xl-start"
                style={{
                  color: "var(--main-color)",
                  fontFamily: "Alfa Slab One",
                }}
              >
                Privacy Policy
              </h1>
              <br />
              <br />
              <p style={{ color: "var(--text-color)" }}>
                By using our Site/Bot, you agree that you have read and agree to
                this policy.
              </p>
              <p style={{ color: "var(--text-color)" }}>
                This is our "Privacy Policy" which sets out the policy which
                governs our use of information you provide in connection with
                the XGN BOT website. The terms "you" and "your" refer to all
                individuals or entities accessing this website. The terms "we,"
                "us," "our," refer to XGN BOT and "bot" refers to our Discord
                bot itself.
              </p>
              <p style={{ color: "var(--text-color)" }}>
                We may update this Privacy Policy from time to time. Changes in
                our Privacy Policy will be effective immediately. If you are a
                regular visitor to this website, we recommend that you check
                this Privacy Policy on a regular basis. By using the website
                and/or bot, you consent to the collection, use and transfer of
                your information in accordance with this Privacy Policy. If you
                do not agree to this Privacy Policy, please do not use this
                website or our bot.
              </p>
              <h1>Data collection/use</h1>
              <p style={{ color: "var(--text-color)" }}>
                At our website, we only collect personally identifiable
                information from individuals that they provide to us
                voluntarily. This means we do not require you to register or
                provide information to us in order to view our website. XGN BOT
                only gathers personally identifiable data through our website,
                such as an email address, when voluntarily submitted by a
                visitor. Once collected, we may combine this information with
                other information collected from external sources.
              </p>
              <p style={{ color: "var(--text-color)" }}>
                And then we use them:
              </p>
              <ul>
                <li>To present our website and its contents to you.</li>
                <li>
                  To provide you with information on programs, services or
                  products.
                </li>
                <li>To fulfill any other purpose for which you provide it.</li>
                <li>
                  To notify you about changes to our website, bot or any items
                  that we may offer through it.
                </li>
                <li>
                  To improve our marketing and promotional efforts, to
                  statistically analyze site usage, to improve our content and
                  product offerings, and to customize our site’s content, layout
                  and services.
                </li>
                <li>
                  To request additional information from you for various
                  purposes.
                </li>
                <li>
                  In any other way we may describe when you provide the
                  information.
                </li>
                <li>For any other purpose with your consent.</li>
              </ul>

              <h2>Third-party Websites</h2>
              <p style={{ color: "var(--text-color)" }}>
                This website or messages distributed by our bot may contain
                links to third-party websites. These linked websites are not
                under our control, and we are not responsible for the privacy
                practices or the contents of any such linked website or any link
                contained in any linked website. We provide such links only as a
                convenience, and the inclusion of a link on the website does not
                imply endorsement of the linked website by XGN BOT. If you
                provide any personal data through any such third-party website,
                your transaction will occur on the third party’s website (not
                this website) and the personal data you provide will be
                collected by and controlled by the privacy policy of that third
                party. We recommend that you familiarize yourself with the
                privacy policies and practices of any third parties. PLEASE NOTE
                THAT THIS PRIVACY POLICY DOES NOT ADDRESS THE PRIVACY OR
                INFORMATION PRACTICES OF ANY THIRD PARTIES.
              </p>

              <h2>Contact Information</h2>
              <p style={{ color: "var(--text-color)" }}>
                To ask questions or comment about this Privacy Policy and our
                privacy practices, please{" "}
                <a href="https://discord.gg/8V62RTS25Q">
                  contact us via Discord.
                </a>
              </p>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};
