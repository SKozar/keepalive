class Keepalive < Formula
  desc "Keep macOS awake for Teams during chosen hours"
  homepage "https://github.com/skozar/keepalive"
  url "https://github.com/skozar/keepalive/releases/download/v#{version}/keepalive"
  version "0.1.0"
  sha256 "8a36f03481dc53c3b6efa8450c0f14afbe7a95f0ce63f1f53b01b632974476c3"

  def install
    bin.install "keepalive"
  end

  def caveats
    <<~EOS
      To start the agent:
        keepalive start

      To run with custom schedule:
        keepalive start --schedule 04:00-12:00 --idle 180

      Logs: ~/Library/Logs/keepalive/keepalive.log

      IMPORTANT: Grant Accessibility permission to keepalive:
        System Settings → Privacy & Security → Accessibility
        Add: #{opt_bin}/keepalive
    EOS
  end
end
