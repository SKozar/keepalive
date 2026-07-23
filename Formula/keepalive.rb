class Keepalive < Formula
  desc "Keep macOS awake for Teams during chosen hours"
  homepage "https://github.com/skozar/keepalive"
  version "0.5.1"
  url "https://github.com/skozar/keepalive/releases/download/v#{version}/keepalive-#{version}.tar.gz"
  sha256 "ace014a50e355584212076ccfb99ceedcbb76a5aa504ad5a857b2e5b186166d7"

  def install
    libexec.install Dir["*"]
    bin.install_symlink libexec/"keepalive"
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
